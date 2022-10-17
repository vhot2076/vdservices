#!/bin/bash
# ip addr show
export HOST="127.0.0.1"
export FHOST="127.0.0.1"
export PORT="8050"
export FPORT="5000"
echo -e "Starting services...\n"
python3 ./gen/flaskgen.py &
python3 ./visual/dashapp.py &
jobs
key="a"
echo -e "\n"
read -t 1 -n 1 key
read -n 1 -p "Press a key for stop services: " key
echo -e "\n"
kill %2
kill %1
read -t 1 -n 1 key
jobs
