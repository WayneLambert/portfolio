import pytest
from django.urls import reverse


@pytest.mark.slow(reason='Scrapes the EU Referendum Results as part of the view')
def test_get_referendum_results(client, request):
    """ Asserts a site visitor can GET the `Referendum Results` screen """
    path = reverse('scraping:referendum')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'