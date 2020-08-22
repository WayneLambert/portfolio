import pytest
from mixer.backend.django import mixer


@pytest.fixture(scope='function')
def post(db, request):
    return mixer.blend('blog.Post')
