# onboarding - Task 0 -> Nivelamento 01

Objetivo: Implementar um Switch e hosts (Computador, Notebook) usando POO.

## Introdução

- Nesta tarefa, deverá ser implementado um switch e hosts simples.
Esse switch e hosts deve ser pensado e modelado usando POO.

## objeto switch simples

- no switch deve ser criado em um arquivo chamado `switch.py` devera conter um metodo chamado `connect_to_port`, `disconnect_to_port` e `get_devices` fora outras funcionalidades como ligar, desligar... 

- `connect_to_port` vai ser usado para criar um link entre o dispositivo e uma porta da do switch e  `disconnect_to_port` para remover o link já criado.
-  `get_devices` deve ser usado para verificar os links alocados no switch

- fazer o uso Recomendado(`Dicionarios`) ou `Lista` para armazenar os hosts.
- criar warnings erros, por exemplo: a tentativa de conectar 2 aparelhos na mesma porta. Obs: o dispositivo pode ser alocado em outra porta aleatoria.
  
- Opcional (*nivel hard*) (dipositivo receber um ip aleatorio quando conectado ao switch)

## objeto host (computador e notebook)
- no hosts deve ser criado um arquivo chamado `hosts.py` e devera conter as classes `Computador-Desktop` e `Notebook`.
- as classes deve ser criadas levando em consideração caracteristicas importantes para um dispositivo, como `MAC`, `Nome_do_dispositivo`, `Marca`, etc... 
 
## Finalização
- deve ser criação de um arquivo `main.py` para centralizar o codigo.
- realizar a importação das classes `Simple-switch`, `Computador-Desktop` e `Notebook` de seus respectivos arquivos e criar a estrutura de exeção no `main.py`.


- ex de como ficaria no final no arquivo `main.py`:   
```{python}
from Hosts import Notebook, Desktop
from Switch import Switch

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
```

Obs: Sempre comentar o codigo para auxiliar na explicação.

## Recompensas da Task 0
- Desenvolver habilidades é pratica POO, desenvolvendo habilidades como modelagem de um objeto e a comunicação entre classes.
- as abordagem usadas acima facilitara o desenvolvimento nas proximas tasks.
- Auxiliar conceitos como Dicionario, funções(métodos), condicionais e ajudar no desenvolvimento da logica de programação.

# Material
- https://docs.python.org/pt-br/3/tutorial/classes.html
- https://pythonacademy.com.br/blog/introducao-a-programacao-orientada-a-objetos-no-python
- https://panda.ime.usp.br/panda/static/pythonds_pt/01-Introducao/13-poo.html

# Videos que Recomendo
 
- (octavio miranda) https://www.youtube.com/watch?v=RLVbB91A5-8&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7 

- (hash tag treinamentos) https://www.youtube.com/watch?v=gomDSZaay3E&t=2099s&pp=ygUKUE9PIHB5dGhvbg%3D%3D

- (guanabarra) https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&ab_channel=CursoemV%C3%ADdeo (coisas basicas sobre o python e classes no video 117 em diante)


> OBS: essa Task deverar ser entregue via GITHUB.
>
> Todos os arquivos desenvovidos por voce deve ser colocados na pasta chamada `ENTREGA`.



