from flask import Flask, abort,request, jsonify
from mocknet.node import MockBridge
import learning_switch

class App(Flask):

    def __init__(self, topology):
        self.rede = topology
        super().__init__(__name__)
                
    
        @self.route("/get_shortest_path", methods=["GET"])
        def get_shortest_path():
            # pega os parametros no request
            source = request.args.get("source")
            target = request.args.get("target")

            # verificar se os nos existem
            if source not in self.rede.grafo or target not in self.rede.grafo:
                abort(404)

            # calcula o menor caminho
            self.rede.shortest_path(source, target)

            return jsonify("Shortest Path", self.rede.caminho)
        
        @self.route("/switchs", methods=["GET"])
        def get_switchs():
            sw = [i.name for i in self.rede.net.nodes.values() if isinstance(i, learning_switch.SimpleLearningSwitch )]
            return jsonify("Switchs", sw)
        
        @self.route("/hosts", methods=["GET"])
        def get_hosts():
            host = [i.name for i in self.rede.net.nodes.values() if not isinstance(i, learning_switch.SimpleLearningSwitch )]
            return jsonify("hosts", host)
        
        @self.route("/links", methods=["GET"])
        def get_links():
            li = []
            for link in self.rede.net.links:
                li.append((link.adapter1.node.name, link.adapter2.node.name))
            print(li)
            return jsonify("links", li)
        