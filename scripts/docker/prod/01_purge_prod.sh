#!/bin/bash

# Check status of all images, containers and volumes
docker system df -v

# Stop all running containers
docker stop $(docker ps -a -q) portfolio_web_prod portfolio_nginx_prod portfolio_postgres_prod

# Remove all containers
docker rm -f $(docker ps -a -q) portfolio_web_prod portfolio_nginx_prod portfolio_postgres_prod

# Remove all images
docker rmi -f portfolio_web_prod portfolio_nginx_prod portfolio_postgres_prod

# Prune all volumes
docker system prune --volumes -f portfolio_static_prod portfolio_postgres_vol_prod portfolio_media_prod

# Check status of all images, containers and volumes
docker system df -v

# Return message to the user saying complete
echo "***************************************************************************"
echo "PRODUCTION: All of the images, containers and volumes for the ${COMPOSE_PROJECT_NAME} project have been deleted!!"
echo "***************************************************************************"
echo ""