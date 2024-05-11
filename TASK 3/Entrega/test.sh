#!/bin/bash

echo " ------ "
echo "Testando H1 e H3"
echo "O caminho existe esperado o menor caminho"
curl http://127.0.0.1:5000/get_shortest_path?source=h1"&"target=h3

echo " ------ "
echo "Testando H1 e H6"
echo "O host H6 nao existe, esperado o erro 404"
curl http://127.0.0.1:5000/get_shortest_path?source=h1"&"target=h6

echo " ------ "
echo "Testando h1 e H4"
echo "H4 existe, mas nao esta conectado na rede, esperado erro 404"
curl http://127.0.0.1:5000/get_shortest_path?source=h1"&"target=h4
