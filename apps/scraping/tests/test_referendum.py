from django.urls import reverse

import pytest


@pytest.mark.slow(reason='Uses a large cassette storage to test the EU Referendum Results')
@pytest.mark.vcr()
def test_get_referendum_results(client):
    """ Asserts a site visitor can GET the `Referendum Results` screen """
    path = reverse('scraping:referendum')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'
