import pytest

from mixer.backend.django import mixer


@pytest.fixture(scope='function')
def category(db, request):
    return mixer.blend('blog.Category')

@pytest.fixture(scope='function')
def search_terms():
    return ['python', 'PYTHON', 'pyTHon', '01234', '&*^%$']
