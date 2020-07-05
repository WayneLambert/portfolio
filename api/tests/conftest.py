import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def factory(request):
    return RequestFactory()

@pytest.fixture(scope='session')
def li_user(db, request):
    return mixer.blend(get_user_model())

@pytest.fixture(scope='session')
def lo_user(db, request):
    return AnonymousUser()

@pytest.fixture(scope='function')
def category(db, request):
    return mixer.blend('blog.Category')

@pytest.fixture(scope='function')
def post(db, request):
    return mixer.blend('blog.Post')
