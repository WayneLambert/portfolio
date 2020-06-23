# pylint: disable=redefined-outer-name
from django.urls import reverse
from contacts import views as contacts_views


class TestContactView:
    def test_contact(self, request, factory):
        """ Asserts any user can access the `contact` form """
        path = reverse('contacts:contact')
        request = factory.get(path)
        response = contacts_views.contact(request)
        assert response.status_code == 200, 'Should be callable by anyone'


    def test_contact_submitted(self, request, factory):
        """ Asserts any user can access the `contact submitted`
            page upon form submission """
        path = reverse('contacts:contact_submitted')
        request = factory.get(path)
        response = contacts_views.contact_submitted(request)
        assert response.status_code == 200, 'Should be callable by anyone'
