import pytest
from django.contrib.auth import views as auth_views
from django.urls import reverse
from users import views as user_views

pytestmark = pytest.mark.django_db  # Request database access


def test_register(client):
    """ Verify that the registration view is publicly accessible """
    path = reverse('register')
    response = client.get(path)
    assert response.status_code == 200

# FIXME: Needs resolving
class TestLogin:
    def test_login(self, client):
        """ Verify that the login view is publicly accessible """
        path = reverse('login')
        response = client.get(path)
        assert response.status_code == 200
