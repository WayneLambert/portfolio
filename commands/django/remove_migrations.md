# Remove All Django Migrations

This must be run from the project's source directory

`$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`

`$ find . -path "*/migrations/*.pyc"  -delete`

Useful Article: <https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html>
