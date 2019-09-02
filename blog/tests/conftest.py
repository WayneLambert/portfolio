import pytest
from django.contrib.auth.models import User
from django.test import RequestFactory
from mixer.backend.django import mixer


@pytest.fixture
def factory():
    return RequestFactory()


@pytest.fixture
def category(db):
    return mixer.blend('blog.Category')


@pytest.fixture
def post(db):
    return mixer.blend('blog.Post')


@pytest.fixture
def user(db):
    return mixer.blend(User)


@pytest.fixture
def search_terms():
    return ['python', 'PYTHON', 'pyTHon', '01234', '&*^%$']
