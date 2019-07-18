#!/bin/bash

# Check status of all images, containers and volumes
docker system df -v

# Stop all running containers
docker stop | grep *dev*

# Remove all containers
docker rm -f | grep *dev*

# Remove all images
docker rmi -f portfolio_postgres_dev dpage/pgadmin4

# Prune all volumes
docker system prune --volumes -f | grep *dev*

# Check status of all images, containers and volumes
docker system df -v

# Return message to the user saying complete
echo "**************************************************************************"
echo "DEVELOPMENT: All of the images, containers and volumes for the ${COMPOSE_PROJECT_NAME} project have been deleted!!"
echo "**************************************************************************"
echo ""