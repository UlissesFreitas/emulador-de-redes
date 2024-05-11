from mocknet import net
from learning_switch import SimpleLearningSwitch
from topology import Topology
from app import App

net = net.Mocknet()
rede = Topology(net)
myapp = App(rede)

# cria hosts
h1 = net.add_host("h1", mac_address="00:00:00:00:00:01", ipv4_address="10.0.0.1")
h2 = net.add_host("h2", mac_address="00:00:00:00:00:02", ipv4_address="10.0.0.2")
h3 = net.add_host("h3", mac_address="00:00:00:00:00:03", ipv4_address="10.0.0.3")

# cria switchs
s1 = net.add_switch("s1", cls=SimpleLearningSwitch)
s2 = net.add_switch("s2", cls=SimpleLearningSwitch)
s3 = net.add_switch("s3", cls=SimpleLearningSwitch)
h4 = net.add_host("h4", mac_address="00:00:00:00:00:04", ipv4_address="10.0.0.4")

# host to switch
net.add_link(h1, s1)
net.add_link(h2, s1)
net.add_link(h3, s2)

# switch to switch
net.add_link(s1, s2)
net.add_link(s2, s3)

# atualiza os links do grafo
rede.update_edges()

#myapp.run()
