import os

from io import BytesIO

from django.contrib.auth.models import AnonymousUser
from django.core.files.uploadedfile import InMemoryUploadedFile

import pytest

from mixer.backend.django import mixer
from PIL import Image

from apps.blog.models import Category, Post
from apps.blog.tests import helpers


@pytest.fixture(scope='function')
def random_user(django_user_model):
    """ A random user """
    return mixer.blend(django_user_model, pk=2)


@pytest.fixture(scope='function')
def third_user_as_author(django_user_model):
    """ A random user """
    return mixer.blend(django_user_model, pk=3)


@pytest.fixture(scope='function')
def test_password():
    """ A password used for an authenticated user fixture """
    return os.environ['PYTEST_TEST_PASSWORD']


@pytest.fixture(scope='function')
def auth_user(client, django_user_model, test_password):
    """ An authenticated user object using the specified user model """
    user = django_user_model.objects.create_user(
            pk=2,
            first_name='Wayne',
            last_name='Lambert',
            username='wayne-lambert',
            email='wayne-lambert@example.com',
            password=test_password,
    )
    client.login(username=user.username, password=test_password)
    return user


@pytest.fixture(scope='function')
def unauth_user():
    """ An unauthenticated user (i.e. an anonymous user) """
    return AnonymousUser()


@pytest.fixture(scope='function')
def all_users(request, auth_user, unauth_user):
    """
    A combined fixture containing both an authenticated and
    unauthenticated user for testing views that should be available to
    all types of users using parametrization
    """
    user_type = request.param
    users = {
        'auth_user': auth_user,
        'unauth_user': unauth_user,
    }
    return users[user_type]


@pytest.fixture(scope='function')
def fixed_user(django_user_model):
    """
    A fixed user useful in scenarios where testing against known
    instance attributes validates the functionality
    """
    return django_user_model.objects.create_user(
        pk=2,
        first_name='Wayne',
        last_name='Lambert',
        username='wayne-lambert',
        email='wayne-lambert@example.com',
    )


@pytest.fixture(scope='function')
def li_sec_user(django_user_model, client, test_password, **kwargs):
    """
    Useful in tests where a secondary user tries to access a protected
    view and should therefore be greeted within a forbidden response
    """
    if 'username' not in kwargs:
        kwargs['username'] = 'endeavour-morse'
        kwargs['first_name'] = 'Endeavour'
        kwargs['last_name'] = 'Morse'
        kwargs['email'] = 'endeavour-morse@example.com'
    user = django_user_model.objects.create_user(pk=3, **kwargs)
    client.login(username=user.username, password=test_password)
    return user


@pytest.fixture(scope='function')
def pub_post(random_user):
    """ A random published blog post """
    return mixer.blend(Post, author=random_user, status=1)


@pytest.fixture(scope='function')
def draft_posts(third_user_as_author):
    """ A random set of 10 draft blog posts """
    return mixer.cycle(10).blend(Post, author=third_user_as_author, status=0)


@pytest.fixture(scope='function')
def pub_posts(third_user_as_author):
    """ A random set of 10 published blog posts """
    return mixer.cycle(10).blend(Post, author=third_user_as_author, status=1)


@pytest.fixture(scope='function')
def category():
    """ A random blog category """
    return mixer.blend(Category, pk=1)


@pytest.fixture(scope='function', params=helpers.get_search_strings())
def search_terms(request):
    """ A fixture for parametrizing search terms in tests """
    return request.param


@pytest.fixture(scope='function')
def test_image():
    """ A sample in-memory image for tests involving images """
    image = Image.new(mode='RGB', size=(200, 200))
    image_io = BytesIO()
    image.save(image_io, 'JPEG')
    image_io.seek(0)

    return InMemoryUploadedFile(file=image_io, field_name=None,
                                name='test-image.jpg', content_type='image/jpeg',
                                size=len(image_io.getvalue()), charset=None)


@pytest.fixture(scope='function')
def sample_post_data():
    """ A set of form data for completing a blog post form """

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
    """ A set of form data for completing a user registration form """

    return {
        'username': 'wayne-lambert',
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'password1': test_password,
        'password2': test_password,
    }
