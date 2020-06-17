from django.urls import path

from .views import contact, contact_submitted

app_name = 'contacts'

urlpatterns = [
    path('', contact, name='contact'),
    path('submitted/', contact_submitted, name='submitted'),
]
