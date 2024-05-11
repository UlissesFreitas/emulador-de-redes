from Hosts import *
from Switch import Switch


if __name__ == '__main__':

    s1 = Switch(name="s1", brand="cisco", ports=12)
    h1 = Notebook(name="h1", brand="Samsung", mac="00:00:00:00:00:01",velocidade="100mbs")
    h2 = Notebook(name="h2", brand="LeNOVO", mac="00:00:00:00:00:02",velocidade="100mbs")
    h3 = Desktop(name="h3", brand="Dell", mac="00:00:00:00:00:03",velocidade="100mbs")
    h4 = Desktop(name="h4", brand="ASUS", mac="00:00:00:00:00:04",velocidade="100mbs")
    h5 = Desktop(name="h5", brand="Apple", mac="00:00:00:00:00:05",velocidade="100mbs")
    s1.connect_to_port(h1, 1)
    s1.connect_to_port(h1, 12)  # Tentativa de alocar um dipositivo em 2 portas diferentes, Espera-se um erro.
    s1.get_devices()
    s1.connect_to_port(h2, 26)  # porta errada, Espera-se um erro.
    s1.connect_to_port(h2, 12)
    s1.get_devices()
    s1.desconnect_to_port(2)
    s1.get_devices()
    s1.connect_to_port(h3, 2)
    s1.connect_to_port(h4, 3)
    s1.connect_to_port(h4, 0)  # porta errada, Espera-se um erro.
    s1.connect_to_port(h5, 8)
    s1.get_devices()