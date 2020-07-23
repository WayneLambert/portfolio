""" Contacts App: Tests Helpers

The `captcha` field defined in `forms.py` is defined as a key in the
`contact_data` dict. The `PASSED` argument is supplied for testing so
the reCAPTCHA challenge will pass and the form will successfully post.
"""

contact_data = {
    'first_name': 'Wayne',
    'last_name': 'Lambert',
    'email': 'wayne.lambert@example.com',
    'message': 'Test Message',
    'captcha': 'PASSED',
}


form_data = [
    # 01 - True as all valid field entries
    ('Wayne', 'Lambert', 'wayne.lambert@example.com', 'Test Message', True, True),

    # 02 - False as invalid email address (missing `@`)
    ('Wayne', 'Lambert', 'wayne.lambertexample.com', 'Test Message', True, False),

    # 03 - False as invalid email address (missing `.com`)
    ('Wayne', 'Lambert', 'wayne.lambert@example', 'Test Message', True, False),

    # 04 - False as first name is mandatory, therefore cannot be blank
    ('', 'Lambert', 'wayne.lambert@example.com', 'Test Message', True, False),

    # 05 - False as last name is mandatory, therefore cannot be blank
    ('Wayne', '', 'wayne.lambert@example.com', 'Test Message', True, False),

    # 06 - True as even though the reCAPTCHA fails, Google's test keys for dev always pass
    ('Wayne', 'Lambert', 'wayne.lambert@example.com', 'Test Message', False, True),
]
