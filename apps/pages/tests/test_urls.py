from django.urls import reverse

from pages.views import (
    PortfolioView,
    SiteHomeView,
)


class TestUrls:
    def test_home(self):
        """Verify that the `home` url invokes intended view"""
        path = reverse("pages:home")
        assert path, SiteHomeView.as_view().__name__

    def test_portfolio(self):
        """Verify that the `portfolio` url invokes intended view"""
        path = reverse("pages:portfolio")
        assert path, PortfolioView.as_view().__name__
