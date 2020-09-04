""" Helper functions to facilitate the testing of the user application """

import os


def get_sample_form_data():
    return {
        'username': 'wayne-lambert',
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'password1': os.environ['PYTEST_TEST_PASSWORD'],
        'password2': os.environ['PYTEST_TEST_PASSWORD'],
    }
