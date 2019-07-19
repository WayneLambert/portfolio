#!/bin/bash

# Django setup commands
docker-compose exec web_dev python3 manage.py makemigrations users
docker-compose exec web_dev python3 manage.py makemigrations contacts
docker-compose exec web_dev python3 manage.py makemigrations blog
docker-compose exec web_dev python3 manage.py migrate
docker-compose exec web_dev python3 manage.py createsuperuser