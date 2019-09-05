import pytest
from django.contrib.auth.models import User

# Helper function to create a logged in and logged out user
lilo_users = (
    User('li_user', pytest.fixture('li_user')),
    User('lo_user', pytest.fixture('lo_user')),
)
