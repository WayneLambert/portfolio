#!/bin/bash

# Now the project has been pushed up onto Docker Hub, run the following:
git clone https://github.com/WayneLambert/portfolio.git
docker pull waynelambert/portfolio:201907192100_web_prod
docker pull waynelambert/portfolio:201907192100_nginx_prod
docker pull waynelambert/portfolio:201907192100_postgres_prod