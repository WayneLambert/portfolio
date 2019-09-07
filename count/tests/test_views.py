# pylint: disable=redefined-outer-name
from django.urls import reverse
from count import views as count_views


def test_check_count(request, factory):
    """ Asserts any user can access the `check count` page """
    path = reverse('check-count')
    request = factory.get(path)
    response = count_views.check_count(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_count(request, factory):
    """ Asserts any user can access the `count` page """
    path = reverse('count') + '?fulltext=Lorem+ipsum'
    request = factory.get(path)
    response = count_views.count(request)
    assert response.status_code == 200, 'Should be callable by anyone'
