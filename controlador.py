from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr

log = core.getLogger()


def _handle_ConnectionUp(event):
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_NORMAL))
    match = of.ofp_match(dl_type = 0x800)
    match.nw_src = '10.0.0.9'
    match.nw_dst = '10.0.0.1'
    msg.match = match
    #msg.match = of.ofp_match(,nw_src='10.0.0.9')
    event.connection.send(msg)
    log.info("Hubifying %s", dpidToStr(event.dpid))





def _handle_PacketIn(event):
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch(reactive = False):
    if reactive:
        core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
        log.info("Reactive hub running")
    else:
        core.openflow.addListenerByName("ConnectionUp",_handle_ConnectionUp)
        log.info("Proactive hub running")
