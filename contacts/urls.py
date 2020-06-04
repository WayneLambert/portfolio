from django.urls import path
from contacts import views as contacts_views


app_name = 'contacts'

urlpatterns = [
    path('', contacts_views.contact, name='contact'),
]
