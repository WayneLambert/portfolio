from django.urls import path

from apps.contacts.views import ContactFormView, ContactSubmittedView


app_name = "contacts"

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("submitted/", ContactSubmittedView.as_view(), name="submitted"),
]
