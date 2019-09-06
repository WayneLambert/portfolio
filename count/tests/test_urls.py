from django.urls import resolve, reverse


def test_check_count():
    path = reverse('check-count')
    assert resolve(path).view_name == 'check-count'


def test_count():
    path = reverse('count')
    assert resolve(path).view_name == 'count'
