import networkx as nx
import matplotlib.pyplot as plt

class Topology:

    def __init__(self, net):
        self.net = net
        self.grafo = nx.Graph()
        self.update()
        self.caminho = []

    def __repr__(self):
        return self.grafo

    def shortest_path(self, inicio, fim):
        self.update()
        try:
            self.caminho = nx.shortest_path(self.grafo, source=inicio, target=fim)
        except:
            self.caminho = []

    def update(self):
        self.grafo = nx.Graph()

        for host in self.net.hosts:
            self.grafo.add_node(host.name)
            

        for link in self.net.links:
            self.grafo.add_edge(link.intf1.node.name, link.intf2.node.name)
        

    def show_topology(self):
        self.update_edges()
        nx.draw_networkx(self.grafo)
        plt.axis("off")
        plt.show()

