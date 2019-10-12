# pylint: disable=redefined-outer-name
from django.urls import reverse
from text_analysis import views as text_analysis_views


def test_analyse(request, factory):
    """ Asserts any user can access the `analyse` page """
    path = reverse('analyse')
    request = factory.get(path)
    response = text_analysis_views.analyse(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_analysis(request, factory):
    """ Asserts any user can access the `analysis` page """
    path = reverse('analysis') + '?fulltext=Lorem+ipsum'
    request = factory.get(path)
    response = text_analysis_views.analysis(request)
    assert response.status_code == 200, 'Should be callable by anyone'
