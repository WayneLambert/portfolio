from django.urls import path
from contacts import views as contacts_views


urlpatterns = [
    path('', contacts_views.contact, name='contact'),
]
