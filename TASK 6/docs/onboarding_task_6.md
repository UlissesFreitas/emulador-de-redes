# Tarefa 06 do onboarding

Objetivo: Adicionar controladores SDN à topologia sob demanda.

## Introdução

Nesta task do Onboarding, a aplicação desenvolvida nas tasks anteriores terá sua funcionalidade estendida para adicionar controladores SDN ao Mininet.
A API Flask deverá ter uma nova rota, a `/controller `. Ela deve aceitar apenas o método HTTP POST, e sua função é criar um controlador na topologia.
Nos dados fornecidos no corpo request, deverão estar o nome do controlador SDN e o tipo de controlador ("remote" ou "reference"). Caso seja reference,
a app deve adicionar à rede Mininet um controller referência (`mininet.node.Controller ou mininet.node.OVSController`). No entanto, caso o tipo seja remote, a app deve utilizar a 
[biblioteca Python para a Docker Engine](https://docker-py.readthedocs.io/en/stable/) para executar um container do controlador ONOS [Documentação Onos](https://wiki.onosproject.org/display/ONOS/Tutorials). É importante chamar o método `start()` do controlador SDN criado ex: c1.start(), e que o nome do controlador SDN seja único na rede.

- Obs.: Caso seja remoto, o endereço IP do controlador SDN deve ser informado quando o controlador for adicionado ao Mininet.
- Após criar um novo Link é necessario usar o comando Switch.start([controlador]) para ele identificar que o link novo existe. 

Além disso, é fundamental que os switches adicionados criados via `POST /switch` sejam iniciados e associados a algum controlador. Esse dado deve ser informado no corpo da request, juntamente com parâmetros opcionais que devem ser passados para o método `addSwitch` do Mininet.
A app deve, ainda, ter uma rota `/controllers` que aceite o método HTTP GET e retorne uma lista com todos os controladores da rede e indique o tipo de cada um.
Por fim, o script shell de teste deverá incluir testes para as novas rotas implementadas na task 06.

### Dicas sobre a imagem ONOS
Sinta-se livre para usar a sua criatividade nesta TASK, aqui estão alguns passos que podem te ajudar! 
- Opcional: Crie um Arquivo chamado client_docker.py com uma classe `Client_docker()`, com um método chamado `run_container()` que quando chamado execute o container do ONOS e retorne o ip que deverar ser usado na classe `mininet.node.RemoteController`, faça o import da classe no app.py e use-a para a criação da imagen do ONOS para o novos Controllers.

- Use a imagem oficial do ONOS ->  `onosproject/onos`
- Tente usar o comando `container.logs()` para capturar os Logs do container Docker.
- Após o container Docker ser inicializado, é necessário esperar a aplicação web ser inicializada, a mesma pode ser identificada pela seguinte linha no log:
  - `"Started HttpServiceContext{httpContext=WebAppHttpContext{org.onosproject._onos-gui2-base-jar - 202}}"`
  
  >Atenção use um `docker run -it onosproject/onos` para verifica se a saida acima encontra-se nos logs!
- Recorra aos logs para identificar, quando a aplicação web for inicializada, e use o comando `/root/onos/bin/onos-app` dentro do container do ONOS para ativar os seguintes apps para habilitar o envio e recebimento de dados:
  1. `org.onosproject.openflow`
  2. `org.onosproject.fwd`
- Caso o switch tenha um controlador remoto, os seguintes parâmetros devem ser adicionados na sua criação via `POST /switch` para que eles funcionem com o ONOS.
  * `cls=OVSKernelSwitch, protocols=["OpenFlow10"]` 
  * exemplo: 
  net.addSwitch("s1",cls=OVSKernelSwitch, protocols=["OpenFlow10"])
  
  > verifique o vídeo no material complementar.

### Material complementar

- [BUILD YOUR OWN DOCKER USING DOCKER SDK AND PYTHON || Docker SDK 101
](https://www.youtube.com/watch?v=uo_QN_Dx4oQ&ab_channel=FutureAutomation)
- [ONOS SDN Controller Tutorial](https://www.youtube.com/watch?v=IWdYWBMr8Go)
- [Como configurar o ONOS para ser o controlador de uma rede Mininet](https://www.youtube.com/watch?v=7d44rAIIOY0)


## Fatores de avaliação
- No fim do `main.py` seu codigo precisa terminar com as linhas abaixo: (importa o CLI -> `from mininet.cli import CLI`)
```python3
net.build()
net.start()
CLI(net)
net.stop()
```


### main.py
```
... ... ...
...
net.add("h1")
... "h2"
... "h3"
... "s1"
... "c0"
... link(h1,s1)
... link(h2,s1)
... link(h3,s1)
s1.start([c0])
...
... ... ... 
```
> main.py deve ter os seguintes hosts, switches , links, etc ...

### Script.sh:
```bash
#!/bin/bash
#-----------HOSTS---------------------------#
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h4\"}
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h5\"}
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h6\"}
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h7\"}
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h8\"}
curl -X  "POST" http://127.0.0.1:5000/host -H 'Content-Type: application/json' -d {\"name\":\"h9\"}
#-----------CONTROLADOR---------------------#
curl -X "POST" http://127.0.0.1:5000/controller -H 'Content-Type: application/json' -d {\"name\":\"c1\"\,\"tipo\":\"remote\"}
curl -X "POST" http://127.0.0.1:5000/controller -H 'Content-Type: application/json' -d {\"name\":\"c2\"\,\"tipo\":\"reference\"}
curl -X "POST" http://127.0.0.1:5000/controller -H 'Content-Type: application/json' -d {\"name\":\"c3\"\,\"tipo\":\"remote\"}
#-----------SWITCHS-------------------------#
curl -X  "POST" http://127.0.0.1:5000/switch -H 'Content-Type: application/json' -d {\"name\":\"s2\"\,\"controller\":\"c1\"}
curl -X  "POST" http://127.0.0.1:5000/switch -H 'Content-Type: application/json' -d {\"name\":\"s3\"\,\"controller\":\"c2\"}
curl -X  "POST" http://127.0.0.1:5000/switch -H 'Content-Type: application/json' -d {\"name\":\"s4\"\,\"controller\":\"c3\"}
#-----------LINKS---------------------------#
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h4\"\,\"dst\":\"s2\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h5\"\,\"dst\":\"s2\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h6\"\,\"dst\":\"s3\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h7\"\,\"dst\":\"s3\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h8\"\,\"dst\":\"s4\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"h9\"\,\"dst\":\"s4\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"s1\"\,\"dst\":\"s2\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"s2\"\,\"dst\":\"s3\"}
curl -X "POST" http://127.0.0.1:5000/link -H 'Content-Type: application/json' -d {\"src\":\"s3\"\,\"dst\":\"s4\"}
# Deve ser bem sucedido!
```

## Avaliação:

```
mininet>pingall()
...
...
```

> Obs: deve acontecer o ping entre todos os hosts. 

## Demais ajustes

Utilizar o formatador `black` para padronizar o estilo do código.

```bash
pip install black
```

Crie uma copia da pasta Entregas para Entregas_com_black com os codigos formatados com `black`!

## Entrega Final 13/05/2024 (Boa Sorte!)
- Todos os arquivos utilizados.
- Sempre comentar os codigos para facilitar a explicação.