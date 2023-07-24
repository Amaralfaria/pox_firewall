from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import pox.lib.packet as  pkt

log = core.getLogger()


def _handle_ConnectionUp(event):
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_NORMAL))
    match = of.ofp_match(dl_type = 0x800)

    match.nw_src = IPAddr('10.0.0.1')
    match.nw_dst = IPAddr('10.0.0.2')

    #msg.match = match
    msg.priority = 10

    event.connection.send(msg)
    log.info("Hubifying %s", dpidToStr(event.dpid))

    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
    msg.match = match
    msg.priority = 12



    event.connection.send(msg)



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

