import pytest
from django.contrib.auth.models import User

lilo_users = (
    User('li_user', pytest.fixture('li_user')),
    User('lo_user', pytest.fixture('lo_user')),
)
