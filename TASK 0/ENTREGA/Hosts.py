
class Host():
    def __init__(self, name: str, brand: str, mac: str, velocidade: str = '100mbs'):
        self.nome = name
        self.marca = brand
        self.velocidade = velocidade
        self.mac_addr = mac
        self.ip = "0.0.0.0"

    def __repr__(self) -> str:
        return "Nome: " + self.nome +", IP: "+ self.ip + ", Marca: " + self.marca 

        

class Desktop(Host):
    def __init__(self, name: str, brand: str, mac: str, velocidade: str):
        super().__init__(name, brand, mac, velocidade)



class Notebook(Host):
    def __init__(self, name: str, brand: str, mac: str, velocidade: str):
        super().__init__(name, brand, mac, velocidade)
