#!/bin/bash

cont1=`docker container run -dp 8001:8000 myapp`
cont2=`docker container run -dp 8002:8000 myapp`
cont3=`docker container run -dp 8003:8000 myapp`

echo "Testando hosts no container 1"
curl http://127.0.0.1:8001/hosts

echo "Testando switchs no container 2"
curl http://127.0.0.1:8002/switchs

echo "Testando links no container 3"
curl http://127.0.0.1:8003/links

docker container stop $cont1
docker container stop $cont2
docker container stop $cont3
