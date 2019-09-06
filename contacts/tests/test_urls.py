from django.urls import resolve, reverse


def test_contact():
    path = reverse('contact')
    assert resolve(path).view_name == 'contact'
