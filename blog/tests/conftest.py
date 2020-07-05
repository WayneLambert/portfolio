import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from mixer.backend.django import mixer


@pytest.fixture
def factory(request):
    return RequestFactory()

@pytest.fixture
def user(db, request):
    return mixer.blend(User)

@pytest.fixture(scope='session')
def li_user(db, request):
    return mixer.blend(User)

@pytest.fixture(scope='session')
def lo_user(db, request):
    return AnonymousUser()

@pytest.fixture
def category(db, request):
    return mixer.blend('blog.Category')

@pytest.fixture
def post(db, request):
    return mixer.blend('blog.Post')

@pytest.fixture
def search_terms():
    return ['python', 'PYTHON', 'pyTHon', '01234', '&*^%$']
