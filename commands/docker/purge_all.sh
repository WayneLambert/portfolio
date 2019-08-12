#!/bin/bash

# Check status of all images, containers and volumes
docker system df -v

# Stop all running containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm -f $(docker ps -a -q)

# Remove all images
docker rmi -f $(docker images -a -q)

# Prune all volumes
docker system prune --volumes -f

# Check status of all images, containers and volumes
docker system df -v
