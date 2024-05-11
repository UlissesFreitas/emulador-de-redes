from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

from topology import Topology
from app import App


setLogLevel( 'info' )

net = Mininet(controller=Controller, waitConnected=True)
rede = Topology(net)
myapp = App(rede)

# manter ou remover eis a questao
info('*** Criando o controller ***\n')
c0 = net.addController('c0',cls=Controller)

# cria hosts
info('*** Criando os hosts ***\n')
h1 = net.addHost("h1", ipv4_address="10.0.0.1")
h2 = net.addHost("h2", ipv4_address="10.0.0.2")

# cria switchs
info('*** Criando os switchs ***\n')
s1 = net.addSwitch("s1")

# host to switch
info('*** Criando os links ***\n')
net.addLink(h1, s1)
net.addLink(h2, s1)


info( '*** Starting network\n')
s1.start([c0])


# atualiza os links do grafo
rede.update()



# roda o app
myapp.run()

# para o funcionamento da rede
info( '*** Stoping network\n')
net.stop()

