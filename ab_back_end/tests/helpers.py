import pytest
from django.contrib.auth import get_user_model

# Helper function to create a logged in and logged out user
user_types = ('logged_in_user', 'logged_out_user')
lilo_users = (
    get_user_model()('li_user', pytest.fixture('li_user')),
    get_user_model()('lo_user', pytest.fixture('lo_user')),
)


# Helper function to add Middleware to a request
def add_middleware_to_request(request, middleware_class):
    middleware = middleware_class()
    middleware.process_request(request)
    request.session.save()
    return request
