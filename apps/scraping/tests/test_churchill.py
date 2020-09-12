from django.urls import reverse

import pytest


@pytest.mark.vcr()
def test_get_churchill_speech_view(client):
    """ Asserts a site visitor can GET the `Churchill Speech` screen """
    path = reverse('scraping:churchill_speech')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'
