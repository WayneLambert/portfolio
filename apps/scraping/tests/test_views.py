from django.urls import reverse

from apps.scraping.views import ScrapingOptionsView


class TestScrapingOptionsView:
    def test_scraping_options_view(self, factory):
        """ Asserts any user can access `scraping options` page """
        path = reverse('scraping:scraping_options')
        request = factory.get(path)
        response = ScrapingOptionsView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by logged in/out user'
