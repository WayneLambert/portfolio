from django.urls import reverse


def test_get_gettysburg_speech_view(client):
    """ Asserts a site visitor can GET the `Gettysburg Speech` screen """
    path = reverse('scraping:gettysburg_speech')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'
