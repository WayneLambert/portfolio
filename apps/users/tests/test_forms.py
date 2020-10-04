import pytest

from apps.users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestUserRegisterForm:

    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'validity')

    good_data = {
        'username': 'wayne-lambert',
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'password1': 's@mple-p@$$w0rd',
        'password2': 's@mple-p@$$w0rd',
        'validity': True,
    }

    dirty_data = {
        'username': 'Wayne-lambert                 ',  # Notice trailing spaces
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'password1': 's@mple-p@$$w0rd',
        'password2': 's@mple-p@$$w0rd',
        'validity': True,
    }

    def test_form_tests_for_all_fields(self):
        """ Asserts all fields that need to be tested are present """
        form = UserRegisterForm()
        for field in self.fields:
            if field != 'validity':
                assert field in form.fields

    def test_form_is_valid(self):
        """ Asserts correctly filled in form is valid """
        form = UserRegisterForm(data=self.good_data)
        assert form.is_valid(), 'Should be valid'

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = UserRegisterForm(data={})
        assert not form.is_valid(), 'Should be invalid'

    def test_invalid_email_means_invalid_form(self):
        """ Asserts an invalid email filled in form is valid """
        form = UserRegisterForm(data=self.good_data)
        form.data['email'] = 'test-emailexample.com'
        assert not form.is_valid(), 'Should be invalid'
        assert form.errors
        assert form.errors['email'][0] == 'Enter a valid email address.'

    def test_username_is_cleaned(self):
        """
        Asserts username is cleaned by making it lowercase and removing
        the trailing spaces
        """
        form = UserRegisterForm(data=self.dirty_data)
        assert len(form.data['username']) == 30, \
            'With trailing spaces in form submission, the field is 30 chars in length.'
        form.save(commit=False)
        assert form.cleaned_data['username'] == 'wayne-lambert', 'Username has been trimmed'
        assert len(form.cleaned_data['username']) == 13, "Example's username is 30 chars in length"
        assert form.is_valid(), 'Should be valid'


class TestUserUpdateForm:

    fields = ('username', 'email', 'first_name', 'last_name', 'validity')
    good_data = {
        'username': 'wayne-lambert',
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'validity': True,
    }

    dirty_data = {
        'username': 'Wayne-lambert                 ',  # Notice trailing spaces
        'email': 'test-email@example.com',
        'first_name': 'Wayne',
        'last_name': 'Lambert',
        'validity': True,
    }

    def test_form_tests_for_all_fields(self):
        """ Asserts all fields that need to be tested are present """
        form = UserUpdateForm()
        for field in self.fields:
            if field != 'validity':
                assert field in form.fields

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = UserUpdateForm(data={})
        assert not form.is_valid(), 'Should be invalid'

    def test_form_is_valid(self):
        """ Asserts correctly filled in form is valid """
        form = UserUpdateForm(data=self.good_data)
        assert form.is_valid(), 'Should be valid'

    def test_username_is_cleaned(self):
        """
        Asserts username is cleaned by making it lowercase and removing
        the trailing spaces
        """
        form = UserUpdateForm(data=self.dirty_data)
        assert len(form.data['username']) == 30, \
            'With trailing spaces in form submission, the field is 30 chars in length.'
        form.save(commit=False)
        assert form.cleaned_data['username'] == 'wayne-lambert', 'Username has been trimmed'
        assert form.cleaned_data['username'].islower(), 'Username is now in lowercase'
        assert len(form.cleaned_data['username']) == 13, "Example's username is 30 chars in length"
        assert form.is_valid(), 'Should be valid'


class TestProfileUpdateForm:

    fields = ('profile_picture', 'author_view', 'validity')
    good_data_without_image = {
        'profile_picture': '',
        'author_view': 0,
        'validity': True,
    }

    def good_data_with_image(test_image):
        return {
        'profile_picture': test_image,
        'author_view': 0,
        'validity': True,
    }

    def test_form_tests_for_all_fields(self):
        """ Asserts all fields that need to be tested are present """
        form = ProfileUpdateForm()
        for field in self.fields:
            if field != 'validity':
                assert field in form.fields

    def test_empty_form_is_invalid(self):
        """
        Asserts a user clicking `Register` on an empty form returns
        an invalid form
        """
        form = ProfileUpdateForm(data={})
        assert not form.is_valid(), 'Should be invalid'

    def test_form_without_image_is_valid(self):
        """ Asserts correctly filled in form is valid """
        form = ProfileUpdateForm(data=self.good_data_without_image)
        assert form.is_valid(), 'Should be valid'

    def test_form_with_image_is_valid(self):
        """ Asserts correctly filled in form is valid """
        form = ProfileUpdateForm(data=self.good_data_with_image())
        assert form.is_valid(), 'Should be valid'
