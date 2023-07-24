from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import pox.lib.packet as  pkt

log = core.getLogger()

# todo novo switch rodara isso ao se conectar ao POX
def _handle_ConnectionUp(event):


    #Fala pra chegar normalmente em todos os lugares(eu ACHO)
    msg = of.ofp_flow_mod()
    msg.actions.append(of.ofp_action_output(port = of.OFPP_NORMAL))
    match = of.ofp_match(dl_type = 0x800) #acho que isso aqui especifica que é  pra pacotes IPV4(acho)

    msg.priority = 10

    event.connection.send(msg)
    log.info("Hubifying %s", dpidToStr(event.dpid))


    #bloqueia pacotes vindos de 10.0.0.9 para todos o hosts
    msg = of.ofp_flow_mod()
    match = of.ofp_match(dl_type = 0x800)
    match.nw_src = IPAddr('10.0.0.9')
    msg.match = match
    msg.priority = 11
    event.connection.send(msg)

    #pacotes com esses IPs src e src serao encaminhados normalmente pq a prioridade eh mais alta
    msg = of.ofp_flow_mod()
    match = of.ofp_match(dl_type = 0x800)
    match.nw_src = IPAddr('10.0.0.9')
    match.nw_dst = IPAddr('10.0.0.1')
    msg.actions.append(of.ofp_action_output(port = of.OFPP_NORMAL))
    msg.match = match
    msg.priority = 12



    event.connection.send(msg)




#def _handle_PacketIn(event):
#    msg = of.ofp_packet_out()
#    msg.data = event.ofp
#    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
#    event.connection.send(msg)

def launch(reactive = False):
    #if reactive:
    #    core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
    #    log.info("Reactive hub running")
    #else:
    core.openflow.addListenerByName("ConnectionUp",_handle_ConnectionUp)
    log.info("Proactive hub running")
