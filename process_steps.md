# Markdown for Possible Setup Shell Script for Django Project

### Add some move file commands into the script to move a file from my snippets folder with some of the important settings that needs to be either run through the shell or integrated within my project's Python files.

DATABASE_NAME='rest_apis'
REPO_NAME='REST_APIS'

dev
mkdir REST-APIs
cd REST-APIs
mkdir src
cd src
git init
git remote add origin https://github.com/WayneLambert/{REPO_NAME}.git
touch .gitignore
*Migrate README.md to here*
*Migrate LICENSE.md to here*
pipenv shell
pipenv install django
pipenv install djangorestframework
pipenv install django-cors-headers
pipenv install django-crispy-forms
pipenv install django-guardian
pipenv install Pillow
pipenv install psycopg2-binary
pipenv install django-debug-toolbar --dev
pipenv install bpython --dev
pipenv install autopep8 --dev
pipenv install markdown --dev
cd src
django-admin startproject _2b .
cd _2b
mkdir static && cd static
mkdir images
cd ..
mkdir templates && cd templates
touch base.html
touch home.html
touch about.html
touch contact.html
django-admin startapp books
code .

echo "Create a database"
psql
CREATE DATABASE {DATABASE_NAME};
exit

Setup the database superuser
django-admin setup superuser
username = 'waynelambert'
email address = 'wayne.a.lambert@gmail.com'
password = 'testing321'
password confirmation = 'testing321'
