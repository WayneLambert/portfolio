import pytest
from django.test import RequestFactory


@pytest.fixture
def factory(request):
    return RequestFactory()
