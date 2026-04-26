from django.urls import reverse

from apps.pages.views import (
    APIReviewView,
    BlogReviewView,
    CountdownLettersReviewView,
    CountdownNumbersReviewView,
    DataScienceReviewView,
    PortfolioView,
    PrivacyPolicyView,
    ScrapingReviewView,
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

    def test_blog_review(self):
        """Verify that the `blog_review` url invokes intended view"""
        path = reverse("pages:blog_review")
        assert path, BlogReviewView.as_view().__name__

    def test_api_review(self):
        """Verify that the `api_review` url invokes intended view"""
        path = reverse("pages:api_review")
        assert path, APIReviewView.as_view().__name__

    def test_countdown_letters_review(self):
        """Verify that the `countdown_letters_review` url invokes intended view"""
        path = reverse("pages:countdown_letters_review")
        assert path, CountdownLettersReviewView.as_view().__name__

    def test_countdown_numbers_review(self):
        """Verify that the `countdown_numbers_review` url invokes intended view"""
        path = reverse("pages:countdown_numbers_review")
        assert path, CountdownNumbersReviewView.as_view().__name__

    def test_scraping_review(self):
        """Verify that the `scraping_review` url invokes intended view"""
        path = reverse("pages:scraping_review")
        assert path, ScrapingReviewView.as_view().__name__

    def test_data_science_review(self):
        """Verify that the `data_science_review` url invokes intended view"""
        path = reverse("pages:data_science_review")
        assert path, DataScienceReviewView.as_view().__name__

    def test_privacy(self):
        """Verify that the `privacy` url invokes intended view"""
        path = reverse("pages:privacy")
        assert path, PrivacyPolicyView.as_view().__name__
