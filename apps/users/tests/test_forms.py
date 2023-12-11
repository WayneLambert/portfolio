import pytest

from apps.users.forms import (
    EmailTokenSubmissionForm,
    ProfileUpdateForm,
    UserRegisterForm,
    UserTOTPDeviceForm,
    UserUpdateForm,
)


pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestUserRegisterForm:
    fields = ("username", "email", "first_name", "last_name", "password1", "password2", "validity")

    good_data = {
        "username": "wayne-lambert",
        "email": "test-email@example.com",
        "first_name": "Wayne",
        "last_name": "Lambert",
        "password1": "s@mple-p@$$w0rd",
        "password2": "s@mple-p@$$w0rd",
        "validity": True,
    }

    dirty_data = {
        "username": "Wayne-lambert                 ",  # Notice trailing spaces
        "email": "test-email@example.com",
        "first_name": "Wayne",
        "last_name": "Lambert",
        "password1": "s@mple-p@$$w0rd",
        "password2": "s@mple-p@$$w0rd",
        "validity": True,
    }

    def test_form_tests_for_all_fields(self):
        """Asserts all fields that need to be tested are present"""
        form = UserRegisterForm()
        for field in self.fields:
            if field != "validity":
                assert field in form.fields

    def test_form_is_valid(self):
        """Asserts correctly filled in form is valid"""
        form = UserRegisterForm(data=self.good_data)
        assert form.is_valid(), "Should be valid"

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = UserRegisterForm(data={})
        assert not form.is_valid(), "Should be invalid"

    def test_invalid_email_means_invalid_form(self):
        """Asserts an invalid email filled in form is valid"""
        form = UserRegisterForm(data=self.good_data)
        form.data["email"] = "test-emailexample.com"
        assert not form.is_valid(), "Should be invalid"
        assert form.errors
        assert form.errors["email"][0] == "Enter a valid email address."

    def test_username_is_cleaned(self):
        """
        Asserts username is cleaned by making it lowercase and removing
        the trailing spaces
        """
        form = UserRegisterForm(data=self.dirty_data)
        assert (
            len(form.data["username"]) == 30
        ), "With trailing spaces in form submission, the field is 30 chars in length."
        form.save(commit=False)
        assert form.cleaned_data["username"] == "wayne-lambert", "Username has been trimmed"
        assert len(form.cleaned_data["username"]) == 13, "Example's username is 30 chars in length"
        assert form.is_valid(), "Should be valid"


class TestUserUpdateForm:
    fields = ("username", "email", "first_name", "last_name", "validity")
    good_data = {
        "username": "wayne-lambert",
        "email": "test-email@example.com",
        "first_name": "Wayne",
        "last_name": "Lambert",
        "validity": True,
    }

    dirty_data = {
        "username": "Wayne-lambert                 ",  # Notice trailing spaces
        "email": "test-email@example.com",
        "first_name": "Wayne",
        "last_name": "Lambert",
        "validity": True,
    }

    def test_form_tests_for_all_fields(self):
        """Asserts all fields that need to be tested are present"""
        form = UserUpdateForm()
        for field in self.fields:
            if field != "validity":
                assert field in form.fields

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = UserUpdateForm(data={})
        assert not form.is_valid(), "Should be invalid"

    def test_form_is_valid(self):
        """Asserts correctly filled in form is valid"""
        form = UserUpdateForm(data=self.good_data)
        assert form.is_valid(), "Should be valid"

    def test_username_is_cleaned(self):
        """
        Asserts username is cleaned by making it lowercase and removing
        the trailing spaces
        """
        form = UserUpdateForm(data=self.dirty_data)
        assert (
            len(form.data["username"]) == 30
        ), "With trailing spaces in form submission, the field is 30 chars in length."
        form.save(commit=False)
        assert form.cleaned_data["username"] == "wayne-lambert", "Username has been trimmed"
        assert form.cleaned_data["username"].islower(), "Username is now in lowercase"
        assert len(form.cleaned_data["username"]) == 13, "Example's username is 30 chars in length"
        assert form.is_valid(), "Should be valid"


class TestProfileUpdateForm:
    fields = ("profile_picture", "author_view", "validity")
    good_data_without_image = {
        "profile_picture": "",
        "author_view": 0,
        "validity": True,
    }

    def good_data_with_image(self):
        return {"profile_picture": self, "author_view": 0, "validity": True}

    def test_form_tests_for_all_fields(self):
        """Asserts all fields that need to be tested are present"""
        form = ProfileUpdateForm()
        for field in self.fields:
            if field != "validity":
                assert field in form.fields

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = ProfileUpdateForm(data={})
        assert not form.is_valid(), "Should be invalid"

    def test_form_without_image_is_valid(self):
        """Asserts correctly filled in form is valid"""
        form = ProfileUpdateForm(data=self.good_data_without_image)
        assert form.is_valid(), "Should be valid"

    def test_form_with_image_is_valid(self):
        """Asserts correctly filled in form is valid"""
        form = ProfileUpdateForm(data=self.good_data_with_image())
        assert form.is_valid(), "Should be valid"


class TestUserTOTPDeviceForm:
    def test_token_field_contains_extra_attrs(self, device_auth_user):
        """
        Asserts token field of the form includes the extra attrs. Other
        form functionality does not need to be tested because the
        form is a subclass of the Two Factor Auth package
        """
        key = device_auth_user.totpdevice_set.latest("id").key
        form = UserTOTPDeviceForm(key=key, user=device_auth_user)
        extra_attrs = (
            "class",
            "title",
            "placeholder",
        )
        token_field_attrs = form.fields["token"].widget.attrs
        for extra_attr in extra_attrs:
            assert extra_attr in token_field_attrs, "Each attr should be present"
        assert len(token_field_attrs) == 8, "Should be 8 attrs. 5 from package and 3 added"


class TestEmailTokenSubmissionForm:
    good_data = {"token": 123456}
    bad_data = {"token": "B@dT0k3n"}

    def test_form_is_valid(self):
        """Asserts correctly filled in form is valid"""
        form = EmailTokenSubmissionForm(data=self.good_data)
        assert form.is_valid(), "Should be valid"

    def test_form_is_invalid_with_string_submission(self):
        """Asserts incorrectly filled in form is invalid"""
        form = EmailTokenSubmissionForm(data=self.bad_data)
        assert not form.is_valid(), "Should be invalid"

    def test_token_field_contains_desired_attrs(self):
        """Asserts token field of the form includes the set attrs."""
        form = EmailTokenSubmissionForm()
        set_attrs = (
            "autofocus",
            "inputmode",
            "autocomplete",
            "class",
            "title",
            "placeholder",
            "min",
            "max",
        )
        token_field_attrs = form.fields["token"].widget.attrs
        for set_attr in set_attrs:
            assert set_attr in token_field_attrs, "Each attr should be present"
        assert len(token_field_attrs) == 8, "Should be 8 attrs set"
