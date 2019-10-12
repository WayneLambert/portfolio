from django.urls import resolve, reverse


def test_analyse():
    path = reverse('analyse')
    assert resolve(path).view_name == 'analyse'


def test_analysis():
    path = reverse('analysis')
    assert resolve(path).view_name == 'analysis'
