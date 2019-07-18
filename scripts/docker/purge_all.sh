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

# Remove any Django migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Check status of all images, containers and volumes
docker system df -v

# Return message to the user saying complete
echo "***************************************************************************************"
echo "All of the images, containers and volumes for the ${COMPOSE_PROJECT_NAME} project have been deleted!!"
echo "***************************************************************************************"
echo ""