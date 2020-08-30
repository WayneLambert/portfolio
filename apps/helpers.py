""" Helper functions to facilitate testing """

import os

from aa_project.settings.base import APPS_DIR


def get_search_strings() -> list:
    """
    Returns a list of search strings to test the search functionality
    """
    search_strings_file = os.path.join(APPS_DIR, 'blog/tests/search_strings.txt')
    with open(search_strings_file, 'r') as f:
        words = [word.strip('\n') for word in f]
    return words


def add_middleware_to_request(request, middleware_class):
    """
    Supports a testing scenario which simulates an active middleware
    session within the lifecycle of a request.
    """
    middleware = middleware_class()
    middleware.process_request(request)
    request.session.save()
    return request
