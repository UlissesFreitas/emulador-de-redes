from Hosts import Host
from random import randint as rd
MIN = 4
MAX = 24

def dhcp():
    hosts = []
    ip = f"{rd(1,254)}.{rd(1,254)}.{rd(1,254)}.{rd(1,254)}"
    
    while ip in hosts:
        ip = f"{rd(1,254)}.{rd(1,254)}.{rd(1,254)}.{rd(1,254)}"
    
    hosts.append(ip)

    return ip

class Switch():

    def __init__(self, name: str, brand: str, ports: int = 4):
        self.nome = name
        self.marca = brand
               
        if ports <= MIN or ports > MAX:
            self.portas = { f"Eth-{k+1}": None for k in range(MIN)}
        else:       
           self.portas = { f"Eth-{k+1}": None for k in range(ports)}



    def __repr__(self) -> str:
        return "Marca: " + self.marca + " - Portas: " + str(len(self.portas))



    def connect_to_port(self, host: Host, porta: int):

        #assert porta > 0 and porta <= len(self.portas), "OutOfRange"
        #assert self.portas[f"Eth-{porta}"] == None, "porta em usos"
        
        if porta <= 0 or porta > len(self.portas):
            print("O numero da porta e invalido")

        elif  self.portas[f"Eth-{porta}"] != None:
            print(f"Ja existe dispositovo conectado nesta porta {porta}")

        elif host in self.portas.values():
            print("Host ja conectado")
        else:
            self.portas[f"Eth-{porta}"] = host
            host.ip = dhcp()


    def desconnect_to_port(self, porta: int):
        
        #assert porta > 0 and porta <= len(self.portas), "OutOfRange"
        #assert self.portas[f"Eth-{porta}"] != None, f"Não existe dispositovo na porta {porta}"

        if porta <= 0 or porta > len(self.portas):
            print("O numero da porta e invalido")

        elif self.portas[f"Eth-{porta}"] == None:
            print(f"Não existe dispositovo na porta {porta}")

        else:
            self.portas[f"Eth-{porta}"] = None


    def get_devices(self):
        print("\t--- Resumo dos Dispositivos ---")
        for porta, host in self.portas.items():
            if host != None:
                print(f"{porta} - {host}")
        print(40*"-")