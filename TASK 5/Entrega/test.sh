#!/bin/bash

echo "*** Enviando Hosts"
curl -X POST -H "Content-type: application/json" -d '{"name":"h3"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h4"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h5"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h6"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h7"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h8"}' http://127.0.0.1:5000/host
curl -X POST -H "Content-type: application/json" -d '{"name":"h9"}' http://127.0.0.1:5000/host

echo "*** Enviando Switches"

curl -X POST -H "Content-type: application/json" -d '{"name":"s2"}' http://127.0.0.1:5000/switch
curl -X POST -H "Content-type: application/json" -d '{"name":"s3"}' http://127.0.0.1:5000/switch

echo "*** Enviando Links"
curl -X POST -H "Content-type: application/json" -d '{"src":"s3", "dst":"s1"}' http://127.0.0.1:5000/link

curl -X POST -H "Content-type: application/json" -d '{"src":"h4", "dst":"s2"}' http://127.0.0.1:5000/link
curl -X POST -H "Content-type: application/json" -d '{"src":"h5", "dst":"s2"}' http://127.0.0.1:5000/link
curl -X POST -H "Content-type: application/json" -d '{"src":"h6", "dst":"s2"}' http://127.0.0.1:5000/link
curl -X POST -H "Content-type: application/json" -d '{"src":"h7", "dst":"s3"}' http://127.0.0.1:5000/link
curl -X POST -H "Content-type: application/json" -d '{"src":"h8", "dst":"s3"}' http://127.0.0.1:5000/link
curl -X POST -H "Content-type: application/json" -d '{"src":"h9", "dst":"s3"}' http://127.0.0.1:5000/link
