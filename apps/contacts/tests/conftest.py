""" Contacts App: Tests Helpers

The `captcha` field defined in `forms.py` is defined as a key in the
`contact_data` dict. The `PASSED` argument is supplied for testing so
the reCAPTCHA challenge will pass and the form will successfully post.
"""

import pytest


@pytest.fixture(scope='function')
def contact_data():
    """ Builds a sample contact for completing a contact form """
    return {
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'email': 'wayne.lambert@example.com',
        'message': 'Test Message',
        'captcha': 'PASSED',
}
