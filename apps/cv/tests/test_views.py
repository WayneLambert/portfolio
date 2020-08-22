# pylint: disable=redefined-outer-name
from django.urls import reverse
from apps.cv.views import CVView


def test_cv(request, factory):
    """ Asserts any user can access the `cv` page """
    path = reverse('cv:cv')
    request = factory.get(path)
    response = CVView.as_view()(request)
    assert response.status_code == 200, 'Should be callable by anyone'
