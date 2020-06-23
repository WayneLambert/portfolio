from django.urls import resolve, reverse


class TestURLs:

    def test_contact(self):
        path = reverse('contacts:contact')
        assert resolve(path).view_name == 'contacts:contact'

    def test_contact_submitted(self):
        path = reverse('contacts:contact_submitted')
        assert resolve(path).view_name == 'contacts:contact_submitted'
