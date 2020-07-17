import pytest
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from mixer.backend.django import mixer


@pytest.fixture(scope='session')
def factory(request):
    """ Sets up a RequestFactory object """
    return RequestFactory()


@pytest.fixture(scope='function')
def user(db, request):
    """ Sets up a random user from the mixer package """
    return mixer.blend(User)


@pytest.fixture(scope='function')
def li_user(db, request):
    """ Sets up readable fixture to emulate a logged in user """
    return mixer.blend(User)


@pytest.fixture(scope='function')
def lo_user(db, request):
    """ Sets up readable fixture to emulate a logged out user """
    return AnonymousUser()



""" ---- Functions to facilitate the marking of `slow` unit tests ---- """

def pytest_addoption(parser):
    """ Sets a command line flag `--runslow` for the CLI """
    parser.addoption(
        '--runslow', action='store_true', default=False, help='run slow tests'
    )

def pytest_configure(config):
    """ Sets tests with the @pytest.mark.slow decorator as the ones to be skipped """
    config.addinivalue_line('markers', 'slow: mark test as slow to run')

def pytest_collection_modifyitems(config, items):
    """
    When `--runslow` is added as a CLI flag, run test marked
    with `slow` decorator, otherwise skip running the test
    """
    if config.getoption('--runslow'):
        return
    skip_slow = pytest.mark.skip(reason='need --runslow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)

""" ---- End Functions Set ---- """
