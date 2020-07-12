import pytest

from contacts.forms import ContactForm


class TestCandidateRegisterForm:

    field_list = ('first_name', 'last_name', 'email', 'message', 'captcha', 'validity')

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

    @pytest.mark.parametrize(argnames=field_list, argvalues=form_data)
    def test_candidate_register_form(
            self, first_name, last_name, email, message, captcha, validity):
        """
        Tests that variations of a contact form entry behaves as expected.
        URL: https://pypi.org/project/django-recaptcha/#local-development-and-functional-testing
        """
        form = ContactForm(data={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message,
            'captcha': captcha,
        })

        assert form.is_valid() is validity, \
            'Assets valid form submission for input variation'
