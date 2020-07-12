from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from mixer.backend.django import mixer

import pytest

@pytest.fixture(scope='session')
def factory(request):
    return RequestFactory()

@pytest.fixture(scope='function')
def user(db, request):
    return mixer.blend(User)

@pytest.fixture(scope='function')
def li_user(db, request):
    return mixer.blend(User)

@pytest.fixture(scope='function')
def lo_user(db, request):
    return AnonymousUser()
