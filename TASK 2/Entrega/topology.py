import networkx as nx
from mocknet import net
#import matplotlib.pyplot as plt

class Topology:

    def __init__(self, net):
        self.net = net
        self.grafo = nx.Graph()
        self.update_edges()


    def __repr__(self):
        return self.grafo

    def shortest_path(self, inicio, fim):
        self.update_edges()
        try:
            self.caminho = nx.shortest_path(self.grafo, source=inicio.name, target=fim.name)
        except:
            print(f"Não foi possivel calcular o caminho entre {inicio.name} e {fim.name}")
            self.caminho = []

    def update_edges(self):
        self.grafo = nx.Graph()
        for link in self.net.links:
            self.grafo.add_edge(link.adapter1.node.name, link.adapter2.node.name)




    def show_topology(self):
        self.update_edges()
        #nx.draw_networkx(self.grafo)
        #plt.axis("off")
        #plt.show()


