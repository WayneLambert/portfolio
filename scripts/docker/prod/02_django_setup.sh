#!/bin/bash

# Remove any Django migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
# Django setup commands
docker exec -it portfolio_web python3 manage.py makemigrations users
docker exec -it portfolio_web python3 manage.py makemigrations contacts
docker exec -it portfolio_web python3 manage.py makemigrations blog
docker exec -it portfolio_web python3 manage.py migrate
docker exec -it portfolio_web python3 manage.py createsuperuser