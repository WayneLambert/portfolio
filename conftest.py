import os

from io import BytesIO

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import RequestFactory

import pytest

from mixer.backend.django import mixer
from PIL import Image


@pytest.fixture(scope='session')
def factory(request):
    """ Sets up a RequestFactory object """
    return RequestFactory()


@pytest.fixture(scope='function')
def random_user(db, request):
    """ Sets up a random user from the mixer package """
    return mixer.blend(get_user_model())


@pytest.fixture(scope='function')
def fixed_user(db, request):
    """ Sets up a fixed user object the mixer package """
    return get_user_model().objects.create(
        first_name='Wayne',
        last_name='Lambert',
        username='wayne-lambert',
        email='test_email@example.com',
    )


@pytest.fixture(scope='function')
def li_user(db, request):
    """ Sets up readable fixture to simulate a logged in user """
    return mixer.blend(get_user_model())


@pytest.fixture(scope='function')
def lo_user(db, request):
    """ Sets up readable fixture to simulate a logged out user """
    return AnonymousUser()


@pytest.fixture(scope='function')
def test_password():
    return os.environ['PYTEST_TEST_PASSWORD']


@pytest.fixture(scope='function')
def li_prim_user(db, request, client, **kwargs):
    if 'username' not in kwargs:
        kwargs['username'] = 'wayne-lambert'
        kwargs['first_name'] = 'Wayne'
        kwargs['last_name'] = 'Lambert'
        kwargs['email'] = 'wayne-lambert@example.com'
    user = get_user_model().objects.create_user(**kwargs)
    client.login(username=user.username, password=test_password)
    return user


@pytest.fixture(scope='function')
def li_sec_user(db, request, client, **kwargs):
    if 'username' not in kwargs:
        kwargs['username'] = 'endeavour-morse'
        kwargs['first_name'] = 'Endeavour'
        kwargs['last_name'] = 'Morse'
        kwargs['email'] = 'endeavour-morse@example.com'
    user = get_user_model().objects.create_user(**kwargs)
    client.login(username=user.username, password=test_password)
    return user


@pytest.fixture(scope='function')
def post(db, request):
    return mixer.blend('blog.Post')


@pytest.fixture(scope='function')
def test_image():
    """ Builds a sample in-memory image for unit tests involving images """
    image = Image.new(mode='RGB', size=(200, 200))  # Create new image using PIL
    image_io = BytesIO()  # Set BytesIO object for saving image
    image.save(image_io, 'JPEG')  # Save image to image_io
    image_io.seek(0)  # Seek to start

    return InMemoryUploadedFile(file=image_io, field_name=None, name='test-image.jpg',
                                content_type='image/jpeg', size=len(image_io.getvalue()),
                                charset=None)


#########################################################################################
  ## Functions to facilitate the marking of `slow` unit tests ##
#########################################################################################

def pytest_addoption(parser):
    """ Sets a command line flag `--runslow` for the CLI """
    parser.addoption(
        '--runslow', action='store_true', default=False, help='run slow tests'
    )


def pytest_configure(config):
    """
    Sets tests with the @pytest.mark.slow decorator as the ones to
    be skipped
    """
    config.addinivalue_line('markers', 'slow: mark test as slow to run')


def pytest_collection_modifyitems(config, items):
    """
    When `--runslow` is added as a CLI flag, run test marked with
    `slow` decorator, otherwise skip running the test
    """
    if config.getoption('--runslow'):
        return
    skip_slow = pytest.mark.skip(reason='need --runslow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)

#########################################################################################
