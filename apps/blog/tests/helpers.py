""" Helper functions to facilitate the testing of the blog application """

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
