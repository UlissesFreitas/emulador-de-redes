from flask import Flask, abort,request, jsonify, make_response
from mininet.node import Controller, RemoteController, OVSController

class App(Flask):

    def __init__(self, topology):
        self.rede = topology
        super().__init__(__name__)
                
    
        @self.route("/get_shortest_path", methods=["GET"])
        def get_shortest_path():
            # pega os parametros no request
            try:
                source = request.args.get("source")
                target = request.args.get("target")
            except:
                abort(400)

            # verificar se os nos existem
            if source not in self.rede.grafo or target not in self.rede.grafo:
                abort(400)

            # calcula o menor caminho
            self.rede.shortest_path(source, target)

            return jsonify("Shortest Path", self.rede.caminho)


        @self.route("/switchs", methods=["GET"])
        def get_switchs():
            sws = [sw.name for sw in self.rede.net.switches]
            return jsonify("Switchs", sws)


        @self.route("/hosts", methods=["GET"])
        def get_hosts():
            hosts = [host.name for host in self.rede.net.hosts]
            return jsonify("hosts", hosts)


        @self.route("/links", methods=["GET"])
        def get_links():
            li =[]# [link for self.rede.net.links]
            for link in self.rede.net.links:
                li.append((link.intf1.name, link.intf2.name))
        
            return jsonify("links", li)
        

        @self.route("/host", methods=["POST"])
        def set_host():
            try:
                host = request.get_json()
            except:
                abort(400)
            
            self.rede.update()

            for h in self.rede.net.hosts:
                if h.name == host['name']:
                    abort(401)

            self.rede.net.addHost(host['name'])

            resp = make_response('',200)            
            return resp
        

        @self.route("/switch", methods=["POST"])
        def set_switch():
            try:
                switch = request.get_json()
            except:
                abort(400)
            
            
            # busca o controller na rede, se nao existir da erro e aborta
            # a funcao get gera um exception caso o obj nao exista
            con=''
            try:
                
                con = self.rede.net.get(switch["controller"])

            except:
                abort(401)


            self.rede.update()

            # melhorar isso depois
            for sw in self.rede.net.switches:
                if sw.name == switch['name']:
                    abort(401)

            self.rede.net.addSwitch(switch['name'])

            # associando o controlador ao switch
            #self.rede.net.get(switch['name']).start()
            #self.rede.net.get(switch["controller"])
            
            self.rede.net.get(switch['name']).start([con])
            print('*** Associando o SWITCH ao Controller')

            resp = make_response('',200)            
            return resp


        @self.route("/link", methods=["POST"])
        def set_link():
            try:
                link = request.get_json()
            except:
                abort(400)
            
            # nem sei se isso ainda e nescessario
            self.rede.update()

            # checa se o host existe na lista com o nome dos hosts e switches

            node_names = [h.name for h in self.rede.net.hosts]
            node_names += [sw.name for sw in self.rede.net.switches]

            if link['src'] not in node_names:
                abort(404)
            
            if link['dst'] not in node_names:
                abort(404)

            # verifica se o link ja existe
            for lk in self.rede.net.links:
                if (lk.intf1.node.name == link['src'] \
                or lk.intf1.node.name == link['dst'] ) \
                and (lk.intf2.node.name == link['src'] \
                or lk.intf2.node.name == link['dst'] ):
                    abort(401)

            self.rede.net.addLink(link['src'], link['dst'])

            resp = make_response('',401)            
            return resp
        

        @self.route("/controller", methods=["POST"])
        def set_controller():
            controlador = request.get_json()


            if controlador['tipo'] == "remote":
                
                try:
                    self.rede.net.get(controlador['name'])
                    print('Controlador ja existe')
                                
                    return '', 401
                    
                except:
                    print('*** Criando Controller')
                    self.rede.net.addController(controlador['name'], controller=RemoteController, ip='172.17.0.2')
                    print('**** Ininciando o Controller')
                    self.rede.net.get(controlador['name']).start()


            elif controlador['tipo'] == "reference":
                # quando eu procuro por um objeto
                # se o obj existir ele retorna o obj
                # caso o obj nao exista da erro
                # if controlador['name'] == self.rede.net.get(controlador['name']):
                # 
                # PROGRAMACAO ORIENTADA A GAMBIARRA
                # EXTREME GO HORSE
                
                #self.rede.net.get(controlador['name'])
                
                try:
                    self.rede.net.get(controlador['name'])
                    print('Controlador ja existe')
                                
                    return '', 401
                    
                except:
                    print('*** Criando Controller')
                    self.rede.net.addController(controlador['name'], cls=Controller)
                    
                
            # se nao for remote nem reference retorna um erro
            else:
                abort(401)

            # debug
            print('++++++++++')
            print(self.rede.net.controllers)

            resp = make_response('',200)            
            return resp