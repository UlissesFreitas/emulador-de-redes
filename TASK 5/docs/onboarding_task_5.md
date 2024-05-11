# Tarefa 05 do onboarding

Objetivo: Utilizar o emulador de redes Mininet no lugar do Mocknet para a aplicação desenvolvida até aqui.

## Introdução

Nesta task do Onboarding, a aplicação desenvolvida nas tasks anteriores será configurada para utilizar o [Mininet](https://mininet.org)
ao invés do Mocknet utilizado até então.
A rede (`net`) criada no arquivo `main.py` deverá ser uma instância da classe `mininet.net.Mininet`, e a classe Topology deverá extrair os dados da topologia desse objeto da classe `Mininet`. 
Nessa topologia, o controlador utilizado será o controlador referência (`mininet.node.Controller`).

O grafo ainda deverá utilizar o networkx, e a app Flask ainda deve retornar as informações corretamente.
Além disso, a app deverá ter mais três rotas/endpoints:
- `/switch`: deve aceitar apenas o método HTTP POST e criar na rede do mininet um switch com o nome passado no corpo da requisição (ex.: `{"name": "s1"}`)
- `/host`: deve aceitar apenas o método HTTP POST e criar na rede do mininet um host com o nome passado no corpo da requisição (ex.: `{"name": "h1"}`)
- `/link`: deve aceitar apenas o método HTTP POST e criar na rede do mininet um link entre os nós passados no corpo da requisição (ex.: `{"src": "h1", "dst", "s1"}`)
No caso dos endpoints `/switch` e `/host`, a app deve verificar se o nó da rede já existe, e caso exista retornar um status HTTP 401.
Já no caso do endpoint `/link`, caso um nó não exista na rede, a app deve retornar 404. Caso o link já exista entre esses dois nós, retornar 401.


## Imagem Docker

Nessa task, não será preciso entregar o Dockerfile e nem seguir a arquitetura da task 04.


## Endpoints novos

- Ver na documentação do Flask como utilizar o método POST e como pegar os dados em JSON do corpo da request.
- Fazer as verificações e acessar o objeto do mininet para a criação de novos nós e links.
- Atualizar o grafo da topologia a cada alteração no mininet.
- Além disso, os endpoints antigos deverão ser atualizados para obter os valores do mininet. (Dica: use dir, semelhante a Task 2)

O script Shell para teste da rede deverá incluir comandos Curl para testar esses novos endpoints também.


## Pontos de Avaliação

O objetivo da Task 5 é que a rede do mininet seja modelada a partir de um script. Desta vez o main.py deverar ter a topologia simples -> "h1, h2 e s1", e após a execução do main.py e do Flask, deverar ser realizadas as requisições conforme abaixo via Curl com o metodo POST para cada endpoint.

endpoints para serem criados:
```bash
Hosts: h3 h4 h5 h6 h7 h8 h9
Switches: s2 s3
Links: (s3,s1),(h4,s2),(h5,s2),(h6,s2),(h7,s3),(h8,s3),(h9,s3)
# OBS 1: Serão 16 requisições!
# OBS 2: adicione pelo menos 3 erros 404, e 2 erros 401!
```

### A funcionalidade desse Scrip exatamente como solicitado acima, será a correção dessa Task em conjunto com a apresentação. O não funcionamento desse script, causará a desclassificação.

## Material de Apoio
- [Introdução ao Mininet](https://www.youtube.com/watch?v=yaleErFDs9w&t=656s)
- [SDN basics](https://www.youtube.com/watch?v=28PTAS3HMJo)
- [Conhecendo o Protocolo OpenFlow](https://www.youtube.com/watch?v=5xbpFajXKJk&t=2058s&pp=ygUVcmFtb24gZm9udGVzIG9wZW5mbG93)


## Arquivos para Entrega
- main.py
- topology.py
- app.py
- Script de execução dos teste

## Entrega dia 06/05 até 12:00 hrs (Entregas posteriores serão desconsideradas)