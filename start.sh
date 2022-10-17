#!/bin/bash
# ip addr show
echo -e "Starting services...\n"
python3 /app/gen/flaskgen.py &
# python3 /app/visual/dashapp.py &
jobs
# echo -e "\nPress Ctrl-D for stop"
# bash

echo -e "\nPress Ctrl-C for stop services\n"
exec python3 /app/visual/dashapp.py
