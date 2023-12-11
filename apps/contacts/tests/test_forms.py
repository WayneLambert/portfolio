import pytest

from contacts.forms import ContactForm

from .helpers import form_data


class TestCandidateRegisterForm:
    field_list = ("first_name", "last_name", "email", "message", "captcha", "validity")

    @pytest.mark.parametrize(argnames=field_list, argvalues=form_data)
    def test_candidate_register_form(
        self, first_name, last_name, email, message, captcha, validity
    ):
        """
        Tests that variations of a contact form entry behaves as expected.
        URL: https://pypi.org/project/django-recaptcha/#local-development-and-functional-testing
        """
        form = ContactForm(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "message": message,
                "captcha": captcha,
            }
        )

        assert form.is_valid() is validity, "Asserts valid form submission for input variation"
