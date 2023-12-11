""" Helper functions to facilitate the testing of the blog application """

import os

from typing import List

from aa_project.settings.base import APPS_DIR


def get_search_strings() -> List:
    """Compiles search strings to test search functionality"""
    search_strings_file = os.path.join(APPS_DIR, "blog/tests/search_strings.txt")
    with open(search_strings_file, "r") as f:
        words = [word.strip("\n") for word in f]
    return words
