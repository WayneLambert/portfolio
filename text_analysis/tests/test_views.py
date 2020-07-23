# pylint: disable=redefined-outer-name
import pytest
from django.urls import reverse


def test_analyse_screen(client, request):
    """ Asserts a site visitor can GET the `analyse` screen """
    path = reverse('text_analysis:analyse')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'

def test_analysis_screen(client, request, text_to_analyse):
    """ Asserts a site visitor can GET the `analysis` screen """
    path = reverse('text_analysis:analysis')
    response = client.get(path, {'fulltext': 'Lorem ipsum dolor sit amet'})
    assert response.status_code == 200, 'Should return with an `OK` status code'
