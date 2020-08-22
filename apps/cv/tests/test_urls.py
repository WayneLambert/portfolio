from django.urls import reverse

from apps.cv.views import CVView


class TestUrls:

    def test_cv(self):
        path = reverse('cv:cv')
        assert path, CVView.as_view().__name__
