from django.urls import reverse

from apps.contacts.views import ContactFormView, ContactSubmittedView


class TestURLs:
    def test_contact(self):
        """Verify that the `contact` url invokes intended view"""
        path = reverse("contacts:contact")
        assert path, ContactFormView.as_view().__name__

    def test_contact_submitted(self):
        """Verify that the `submitted` url invokes intended view"""
        path = reverse("contacts:submitted")
        assert path, ContactSubmittedView.as_view().__name__
