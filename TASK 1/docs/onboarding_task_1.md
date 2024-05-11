# Tarefa para o onboarding

Objetivo: Implementar um SimpleLearningSwitch de camada 2.

## Introdução

Nesta tarefa, deverá ser implementado um switch simples de camada 2.
Esse switch deve encaminhar os frames (quadros) Ethernet (IEEE 802.3) como um switch
de camada 2 tradicional.
Entretanto, para esta tarefa, não será utilizado um switch físico nem um virtualizado ou emulado.
Ao invés disso, será implementado um switch "mock" que apenas simula o funcionamento de um
dispositivo de rede real.
O propósito desta tarefa é que sejam colocadas em prática algumas das tecnologias fundamentais
para o pesquisador de redes de computadores, além de ajudar na familiarização com a linguagem
de programação Python.
A seguir, há uma breve descrição sobre o que são e para que servem os objetos mock.
Além disso, é apresentado o passo a passo lógico do funcionamento esperado do switch.
[Este exemplo](../examples/learning_switch.py) deverá ser utilizado como base para o
desenvolvimento da solução desta tarefa.


## Objetos Mock

Em programação, um objeto [mock](https://en.wikipedia.org/wiki/Mock_object) é aquele que
imita o comportamento de objetos reais de um modo controlado.
Por exemplo, antes de testar uma aplicação web em um servidor http real,
escreve-se um *mock* do server http que imita o funcionamento de um server http real.
Dessa forma, a aplicação web pode ser testada em um ambiente controlado antes de ser
implementada em um ambiente de produção.
Isso é especialmente útil para certificar-se que uma atualização no software não compromete
a funcionalidade da aplicação. 

> Esse é um dos habilitadores do TDD (Test Driven Development).


## Funcionamento de um switch L2

A função de um switch de camada 2 (L2) é receber e enviar quadros Ethernet.
Esse processo é denominado encaminhamento (forwarding).
O switch L2 é um elemento fundamental de toda grande topologia de rede, pois além de separar os
domínios de colisão dos enlaces, o switch L2 inspeciona cada frame e armazena os endereços mac
observados em uma tabela (tabela mac).
O switch L2 utiliza sua tabela mac para encaminhar os frames apenas para a porta física em que 
aquele endereço mac está conectado.


## Lógica de encaminhamento

A grosso modo, o switch L2 deve processar cada pacote recebido da seguinte forma:

- Se o endereço mac de origem não está presente na tabela mac do switch,
  então o switch deve adicionar esse endereço mac à essa tabela para "aprender"
  esse endereço, e associá-lo à porta física em que o quadro foi recebido.
- Se o endereço mac de destino for um endereço broadcast (ff:ff:ff:ff:ff:ff),
  o switch L2 deve encaminhar o pacote a todas as demais portas.
- Se o endereço mac de destino não está presente na tabela mac do switch, então
  o frame deverá ser encaminhado para todas as portas como se seu endereço fosse o
  endereço de broadcast.
- Se o endereço mac de destino já for conhecido, e está presente na tabela mac do switch,
  o frame deverá ser enviado àquela porta física associada àquele endereço mac.

Obs.: Para o endereço de broadcast dos frames ethernet, utilizar o valor da constante
`BROADCAST_MAC_ADDR`, encontrada no módulo `mocknet.proto`.

#
## Atenção para a TASK é necessario instalar o biblioteca mocknet!
#### OBS: Para instalar o mocknet, identificar onde se encontra-se o arquivo setup.py e rodar o comando abaixo para instalar a biblioteca mocknet. 
  `pip install -e .`

### Prazo de entrega: 08/04/2024

#### Entrega esperada!
- Entrega/learning_switch.py