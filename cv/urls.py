from django.urls import path

from .views import CVView

app_name = 'cv'

urlpatterns = [
    path('', CVView.as_view(), name='cv'),
]
