#!/usr/bin/env bash

docker-compose down
docker-compose rm -f
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d