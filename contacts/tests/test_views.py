# pylint: disable=redefined-outer-name
from django.urls import reverse
from contacts import views as contacts_views


def test_contact(request, factory):
    """ Asserts any user can access the `contact` form """
    path = reverse('contact')
    request = factory.get(path)
    response = contacts_views.contact(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_contact_submitted(request, factory):
    """ Asserts any user can access the `contact submitted` page upon form submission"""
    path = reverse('contact-submitted')
    request = factory.get(path)
    response = contacts_views.contact(request)
    assert response.status_code == 200, 'Should be callable by anyone'
