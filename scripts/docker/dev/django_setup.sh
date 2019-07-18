#!/bin/bash

# Remove any Django migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
# Django setup commands
docker-compose exec web_dev python3 manage.py makemigrations users
docker-compose exec web_dev python3 manage.py makemigrations contacts
docker-compose exec web_dev python3 manage.py makemigrations blog
docker-compose exec web_dev python3 manage.py migrate
docker-compose exec web_dev python3 manage.py createsuperuser