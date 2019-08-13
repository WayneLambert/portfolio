# List Django Settings Variables

Lists of all the Django settings within the project's namespace in the terminal.
This can be useful in production in cases where you do not have access to Django Debug Toolbar.

`$ python manage.py diffsettings --all`

In the case of a Linux deployment to production, this would need to be:

`$ docker-compose -f docker-compose.prod.yml exec web python manage.py diffsettings --all`

In the case of a Heroku deployment, this would need to be:

`$ heroku run python manage.py diffsettings --all`
