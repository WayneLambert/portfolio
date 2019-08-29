# PyTest Commands

A list of commands for PyTest. As usual, when developing within a docker container, precede the command with `docker-compose exec web` where web is the canonical name given to the service for my Django project.

## Admin Commands

### Collect a List of All Tests in the Project

$ `pytest --collect-only`

### Run All Tests Not Requiring Database Access

$ `py.test -m 'not django_db`

