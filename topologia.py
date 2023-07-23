from mininet.topo import Topo


class MyTopo(Topo):

    def __init__(self):
        Topo.__init__(self)


        h = []
        h.append(None)
        for i in range(1,11):
            host = self.addHost('h{}'.format(i))
            h.append(host)


        s = []
        s.append(None)
        for i in range(1,5):
            switch = self.addSwitch('s{}'.format(i))
            s.append(switch)

        self.addLink(s[1],s[2])
        self.addLink(s[2],s[3])
        self.addLink(s[3],s[4])


        self.addLink(h[1],s[1])
        self.addLink(h[2],s[1])
        self.addLink(h[3],s[2])
        self.addLink(h[4],s[2])
        self.addLink(h[8],s[4])
        self.addLink(h[9],s[4])
        self.addLink(h[10],s[4])
        self.addLink(h[5],s[3])
        self.addLink(h[6],s[3])
        self.addLink(h[7],s[3])



topos = {'mytopo': (lambda: MyTopo()) }
