# pox_firewall
Pra rodar o controlador salva ele em algum lugar na pasta pox, eu salvei em pox/pox/forwarding. Ai roda ./pox.py forwarding.controlador
Depois roda a topologia, é só colocar sudo mn --custom topologia.py --topo mytopo --controller=remote,ip=127.0.0.1,port=6633
O problema ta la na mensagem que o firewall ta mandando pros switches, pelo que eu entendi ele da match independente dos valores e dropa tudo
ai não da pra fazer ping entre os hosts
