#!/bin/bash

# Push to GitHub: https://github.com/WayneLambert/portfolio
git push -u origin master

# Login to Docker Hub
docker login --username=waynelambert --email=wayne.a.lambert@gmail.com

# Tag the image. This image has other image dependencies which will also be pushed
docker tag portfolio_web_prod:latest waynelambert/portfolio_web_prod:latest

# Push to Docker Hub: https://cloud.docker.com/repository/docker/waynelambert/portfolio
# DANGER: Ensure that the Docker Hub repo is private
docker push waynelambert/portfolio_web_prod:latest