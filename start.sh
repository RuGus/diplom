#!/bin/bash
./wait-for-it.sh rabbit_node:5672
./wait-for-it.sh minio:9000
sleep 10
python src/main.py