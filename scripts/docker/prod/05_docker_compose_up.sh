#!/bin/bash

# Now that the project has been pulled down from Docker Hub,
# run the following script when at 'wayne@server:/var/www/portfolio$'
docker-compose --file code/docker-compose.prod.yml up