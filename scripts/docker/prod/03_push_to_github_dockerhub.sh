#!/bin/bash

# These commands need to be run locally from the 'src' directory

# Push to GitHub: https://github.com/WayneLambert/portfolio
git add .
git commit -m "Adjust Docker config for production"
git push -u origin master

# Login to Docker Hub
docker login --username=waynelambert --email=wayne.a.lambert@gmail.com

# Tag all of the images required to form the full repository's build
docker tag aaefe82913fe waynelambert/portfolio:web_prod
docker tag cae168d980a6 waynelambert/portfolio:nginx_prod
docker tag 596fd60351ca waynelambert/portfolio:postgres_prod

# Push to Docker Hub: https://cloud.docker.com/repository/docker/waynelambert/portfolio
# DANGER: Ensure that the Docker Hub repo is private
docker push waynelambert/portfolio:web_prod
docker push waynelambert/portfolio:nginx_prod
docker push waynelambert/portfolio:postgres_prod