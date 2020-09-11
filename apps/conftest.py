import os

from io import BytesIO

from django.contrib.auth.models import AnonymousUser
from django.core.files.uploadedfile import InMemoryUploadedFile

import pytest

from mixer.backend.django import mixer
from PIL import Image

from apps.blog.models import Category
from apps.blog.tests.helpers import get_search_strings


@pytest.fixture(name='random_user', scope='function')
def random_user(django_user_model):
    """ Sets up a random user using the `mixer` package """
    return mixer.blend(django_user_model)


@pytest.fixture(scope='function')
def test_password():
    """ Sets up a password to be used during the creation of
        authenticated users """
    return os.environ['PYTEST_TEST_PASSWORD']


@pytest.fixture(name='auth_user', scope='function')
def auth_user(client, django_user_model, test_password, **kwargs):
    """ Creates an authenticated user object using the project's
        specified user model """
    auth_user = django_user_model.objects.create_user(
            first_name='Wayne',
            last_name='Lambert',
            username='wayne-lambert',
            email='wayne-lambert@example.com',
            password=test_password,
    )
    client.login(username=auth_user.username, password=test_password)
    return auth_user


@pytest.fixture(name='unauth_user', scope='function')
def unauth_user(request):
    """ Creates an unauthenticated user object (i.e. an anonymous user) """
    return AnonymousUser()


@pytest.fixture(name='all_users', scope='function')
def all_users(request, auth_user, unauth_user):
    """
    Creates a combined fixture containing both an authenticated and
    unauthenticated user for testing views that should be available to
    all types of users using parametrization
    """
    user_type = request.param
    users = {
        "auth_user": auth_user,
        "unauth_user": unauth_user,
    }
    return users[user_type]


@pytest.fixture(name='fixed_user', scope='function')
def fixed_user(django_user_model):
    """ Creates a fixed user object """
    return django_user_model.objects.create_user(
        first_name='Wayne',
        last_name='Lambert',
        username='wayne-lambert',
        email='wayne-lambert@example.com',
    )


@pytest.fixture(name='li_sec_user', scope='function')
def li_sec_user(django_user_model, client, test_password, **kwargs):
    """
    Creates a secondary user. This is used in tests where a secondary
    user tries to access a protected view and should therefore be
    greeted within a forbidden response
    """
    if 'username' not in kwargs:
        kwargs['username'] = 'endeavour-morse'
        kwargs['first_name'] = 'Endeavour'
        kwargs['last_name'] = 'Morse'
        kwargs['email'] = 'endeavour-morse@example.com'
    user = django_user_model.objects.create_user(**kwargs)
    client.login(username=user.username, password=test_password)
    return user


@pytest.fixture(scope='function')
def post(request):
    """ Creates a random blog post fixture """
    return mixer.blend('blog.Post')


@pytest.fixture(scope='function')
def category(request):
    """ Creates a random blog category fixture """
    return mixer.blend('blog.Category')


@pytest.fixture(name='search_terms', scope='function', params=get_search_strings())
def search_terms(request):
    """ Returns a fixture for parametrizing search strings in tests """
    return request.param


@pytest.fixture(scope='function')
def test_image():
    """ Builds a sample in-memory image for tests involving images """
    image = Image.new(mode='RGB', size=(200, 200))
    image_io = BytesIO()
    image.save(image_io, 'JPEG')
    image_io.seek(0)

    return InMemoryUploadedFile(file=image_io, field_name=None,
                                name='test-image.jpg', content_type='image/jpeg',
                                size=len(image_io.getvalue()), charset=None)


@pytest.fixture(scope='function')
def sample_post_data(random_user):
    """ Builds a sample set of form data for completing a blog post form """

    return {
        'title': 'Test title which has a title of between 40 and 60 chars',
        'content': 'Test content',
        'categories': mixer.cycle(2).blend(Category),
        'reference_url': 'https://waynelambert.dev',
        'image': test_image,
        'status': 0,
        'validity': True,
    }


@pytest.fixture(scope='function')
def sample_user_data():
    return {
        'username': 'wayne-lambert',
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'password1': os.environ['PYTEST_TEST_PASSWORD'],
        'password2': os.environ['PYTEST_TEST_PASSWORD'],
    }
