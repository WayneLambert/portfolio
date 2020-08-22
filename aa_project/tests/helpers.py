""" A suite of helper structures and functions that support global
fixtures to simulate frequently used testing scenarios.
"""

from django.contrib.auth import get_user_model

import pytest


# Helper structures to emulate a logged in and logged out user
user_types = ('logged_in_user', 'logged_out_user')
lilo_users = (
    get_user_model()('li_user', pytest.fixture(name='li_user')),
    get_user_model()('lo_user', pytest.fixture(name='lo_user')),
)


def add_middleware_to_request(request, middleware_class):
    """
    Supports a testing scenario which simulates an active middleware
    session within the lifecycle of a request.
    """
    middleware = middleware_class()
    middleware.process_request(request)
    request.session.save()
    return request
