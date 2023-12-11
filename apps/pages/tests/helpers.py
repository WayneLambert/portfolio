""" Helper functions to facilitate the testing of the pages app """

from aa_project.settings import base


def app_names():
    long_form_apps, short_form_apps = base.PROJECT_APPS, []
    short_form_apps.extend(app.split(".")[1] for app in long_form_apps)
    return short_form_apps
