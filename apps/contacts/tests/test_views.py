# pylint: disable=redefined-outer-name
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse

import pytest

from aa_project.tests.helpers import add_middleware_to_request, lilo_users, user_types
from apps.contacts.models import Contact
from apps.contacts.views import ContactFormView, ContactSubmittedView

from .helpers import contact_data


pytestmark = pytest.mark.django_db

@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestGetContactViews:
    def test_contact_form_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `contact` form """
        path = reverse('contacts:contact')
        request = factory.get(path)
        request.user = lilo_users
        response = ContactFormView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_contact_submitted_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `submitted` page upon form submission """
        path = reverse('contacts:submitted')
        request = factory.get(path)
        request.user = lilo_users
        response = ContactSubmittedView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

@pytest.mark.django_db
class TestPostContactView:
    def test_contact_form_post_view(self, request, factory):
        """ Asserts a random visitor can POST a contact form """
        path = reverse('contacts:submitted')
        request = factory.post(path, contact_data)
        request.user = AnonymousUser()
        request = add_middleware_to_request(request, SessionMiddleware)
        response = ContactFormView.as_view()(request, contact_data)
        assert Contact.objects.count() == 1, 'Should have one contact in the DB'
        assert response.status_code == 302, 'Should redirect'
        assert '/submitted/' in response.url, \
            'Should reach `submitted` url pattern -> `contact_submitted` template'