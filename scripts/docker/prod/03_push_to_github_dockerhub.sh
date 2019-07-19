#!/bin/bash

# These commands need to be run locally from the 'src' directory

# Push to GitHub: https://github.com/WayneLambert/portfolio
git push -u origin master

# Login to Docker Hub
docker login --username=waynelambert --email=wayne.a.lambert@gmail.com

# Tag all of the images required to form the full repository's build
docker tag <IMAGE ID> waynelambert/portfolio:web_prod
docker tag <IMAGE ID> waynelambert/portfolio:nginx_prod
docker tag <IMAGE ID> waynelambert/portfolio:postgres_prod

# Push to Docker Hub: https://cloud.docker.com/repository/docker/waynelambert/portfolio
# DANGER: Ensure that the Docker Hub repo is private
docker push waynelambert/portfolio:web_prod
docker push waynelambert/portfolio:nginx_prod
docker push waynelambert/portfolio:postgres_prod