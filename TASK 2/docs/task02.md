# Tarefa 02 do onboarding

Objetivo: Implementar um grafo de topologia com NetworkX.

## Introdução

Nesta tarefa, deverá ser implementado um grafo de uma topologia de rede Mocknet.
Esse grafo deve ser capaz de computar um melhor caminho simples entre dois nós da rede.
O grafo deve ser criado a partir de um objeto da classe `Mocknet` (do módulo `mocknet.net`), já com os hosts e switches criados.
Como base, poderá ser utilizado o arquivo submetido na task anterior, bem como a classe SimpleLearningSwitch implementada.
Um grafo é uma estrutura de dados não-linear muito utilizada nas redes de computadores, e algoritmos de cálculo de 
rotas e caminhos em uma rede dependem diretamente dos grafos para seu funcionamento.
Para o grafo da topologia, deverá ser utilizada a biblioteca Python [NetworkX](https://networkx.org/).

## Topologia

Nessa task, os dados deverão organizar-se em uma classe chamada `Topology`.
Ela deverá possuir o método construtor, que receberá um objeto Mocknet e, com base nos nós existentes nesse objeto Mocknet,
criará um grafo da biblioteca NetworkX com os hosts e switches do Mocknet como os nodes (nós) do grafo e os links como edges do grafo.

- Dica: na classe Mocknet existe duas listas uma com os nodes e outras com os links.
- Dica: use o comando dir() para identificar atributos e métodos de uma classe.
 
## Show Topology

A classe Topology deve ter um método chamado `show_topology`
esse metodo deve mostrar na tela o grafo da topologia criada com os nodes existentes no objeto Mocknet de forma dinamica, dado que independente da quantidade de hosts ou switches adicionados, Devem ser exibidos no grafo sem qualquer modificação no codigo.


## Shortest Path

Além disso, a classe `Topology` terá um método `shortest_path` que receberá como parâmetro os nomes de dois nós da rede Mocknet.
O método deve então computar o melhor caminho entre os dois nós informados pelo networkx e retornar em uma lista os nomes dos nós em ordem
que compõem o caminho.

**ver** https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html


#### Aviso: importante que o grafo seja atualizado antes de solicitar o show_topology ou shortest_path para as proximas tasks.
#### Aviso: sempre comentar o codigo para facilitar na explicação!

#### OBS: Aproveite a Oportunidade para fazer as alterações no learning_switch.py

### Entrega esperada: ate 15/04.
- topology.py
- main.py
- learning_switch.py
