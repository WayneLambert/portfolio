#  ruff: noqa: F401

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "apps.users"

    def ready(self):
        import users.signals
