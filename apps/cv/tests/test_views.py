from django.urls import reverse
from apps.cv.views import CVView


def test_cv(rf):
    """ Asserts any user can access the `cv` page """
    path = reverse('cv:cv')
    request = rf.get(path)
    response = CVView.as_view()(request)
    assert response.status_code == 200, 'Should be callable by anyone'
