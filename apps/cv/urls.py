from django.urls import path

from apps.cv.views import CVView

app_name = 'cv'

urlpatterns = [
    path('', CVView.as_view(), name='cv'),
]
