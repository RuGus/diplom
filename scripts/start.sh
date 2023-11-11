#!/bin/bash
./scripts/wait-for-it.sh rabbit_node:5672
./scripts/wait-for-it.sh minio:9000
python scripts/file_creator.py
sleep 10
python src/main.py