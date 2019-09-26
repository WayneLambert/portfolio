# Docker Initialization Procedure - Development

The development setup makes use of separate Dockerfiles located within their own folder structure. These are all held within the 'docker' folder.

The setup initialises 3 main services.

The postgres service, the pg-admin service and the web service.

- The postgres service is a lightweight implementation using the Alpine image version of Postgres.
- PG-Admin is simply used for database administration, although I actually prefer to use DataGrip.
- The web service depends upon the postgres image being built first. It adds some additional tools and dependencies required for development in addition to some Linux tools such as a better shell which enables better inspection of the container.

It adds all project files, packages and dependencies as laid out in the Pipfile.lock file.

To build each of the images, create instances of the services as containers and spin up the development server, simply use the command `docker-compose up` whilst located within the `src` folder of my project with my Python virtual environment activated.

Once the containers have been fully built, check `localhost:8001`. This will confirm that the web service is up and running and that I can see the skeleton framework of my project. The database will not be available yet.

To check the status of all images, containers and volumes for the Docker project, use the command:

- `docker system df -v`

Remove all files within the migrations folders for each of your Django apps where you use models. You do not want these to be ran when invoking the `migrate` command. You want the `makemigrations` to start afresh based upon the current state of your models.py files for your respective Django apps.

Then run the commands in the following order:

- `docker-compose exec web python3 manage.py makemigrations users`
- `docker-compose exec web python3 manage.py makemigrations contacts`
- `docker-compose exec web python3 manage.py makemigrations blog`
- `docker-compose exec web python3 manage.py migrate`

This should fully migrate all of the database tables without any error. If you would have tried to just migrate from the start, you may have been presented with errors as Django may have gotten confused because the users model was not in place. The users model has signals which connect profile functionality to custom user functionality. If the users migrations are made first, then the migrate command will also action these in addition to all of the standard tables that Django makes.

It is then advisable to set up a superuser so that you can begin to populate the database:

- `docker-compose exec web python manage.py createsuperuser`

The webserver should be up and running on port 8001 at this point. However, if this does need to be restarted, then use the command:

- `docker-compose exec web python manage.py runserver 0.0.0.0:8001`

From this point, the database needs restoring from a backup or by manually populating the data from either within the Django admin or by using DataGrip. Let Django assign the primary keys by using the admin panel. Other fields can be populated using data downloaded previously from DataGrip such as the backup or 'INSERT INTO' scripts.
