#!/bin/sh

if [ "$DB_SERVICE" = "postgres" ]
then
    echo "Waiting for postgres to initialise..."
    while ! nc -z $DB_DOCKER_SERVICE_PROD $DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

exec "$@"