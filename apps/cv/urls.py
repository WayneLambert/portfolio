from django.urls import path

from cv.views import CVView


app_name = "cv"

urlpatterns = [
    path("", CVView.as_view(), name="cv"),
]
