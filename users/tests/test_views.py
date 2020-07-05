import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestUser:
    def test_register(self, client):
        """ Verify that the registration view is publicly accessible """
        path = reverse('blog:users:register')
        response = client.get(path)
        assert response.status_code == 200

    def test_login(self, client):
        """ Verify that the login view is publicly accessible """
        path = reverse('blog:users:login')
        response = client.get(path)
        assert response.status_code == 200
