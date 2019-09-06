# pylint: disable=redefined-outer-name
from django.urls import reverse
from ab_back_end import views as be_views


def test_home(request, factory):
    """ Asserts any user can access the site's home page """
    path = reverse('home')
    request = factory.get(path)
    response = be_views.home(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_contact_form(request, factory):
    """ Asserts any user can access the site's contact form page """
    path = reverse('contact')
    request = factory.get(path)
    response = be_views.contact_form(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_reading_list(request, factory):
    """ Asserts any user can access the site's readling list page """
    path = reverse('reading-list')
    request = factory.get(path)
    response = be_views.reading_list(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_view_cv(request):
    """ Checks CV updates in Amazon S3 maintain the same working URL """
    working_path = 'https://wl-portfolio.s3.eu-west-2.amazonaws.com/documents/cv_wayne_lambert.pdf'
    test_path = f'{be_views.AWS_BUCKET_ADDRESS}'\
        f'{be_views.AWS_DOCUMENTS_FOLDER}{be_views.AWS_CV_FILENAME}'
    assert working_path == test_path, 'Asserts that path has not changed since working config'


def test_about_me(request, factory):
    """ Asserts any user can access the site's 'About Me' page """
    path = reverse('about-me')
    request = factory.get(path)
    response = be_views.about_me(request)
    assert response.status_code == 200, 'Should be callable by anyone'


def test_privacy_policy(request, factory):
    """ Asserts any user can access the site's 'Privacy Policy' page """
    path = reverse('privacy-policy')
    request = factory.get(path)
    response = be_views.privacy_policy(request)
    assert response.status_code == 200, 'Should be callable by anyone'
