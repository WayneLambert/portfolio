from django.urls import reverse

from pages.views import (AboutMeView, APIReviewView, BackEndSkillsView, BlogReviewView,
                         CountdownLettersReviewView, CountdownNumbersReviewView,
                         DataScienceReviewView, FrontEndSkillsView, HomeView,
                         InfrastructureSkillsView, PortfolioView, PrivacyPolicyView,
                         ReadingListView, RouletteReviewView, ScrapingReviewView,
                         SoftwareSkillsView, TextAnalysisReviewView)


class TestUrls:

    def test_home(self):
        """ Verify that the `home` url invokes intended view """
        path = reverse('pages:home')
        assert path, HomeView.as_view().__name__

    def test_portfolio(self):
        """ Verify that the `portfolio` url invokes intended view """
        path = reverse('pages:portfolio')
        assert path, PortfolioView.as_view().__name__

    def test_blog_review(self):
        """ Verify that the `blog_review` url invokes intended view """
        path = reverse('pages:blog_review')
        assert path, BlogReviewView.as_view().__name__

    def test_api_review(self):
        """ Verify that the `api_review` url invokes intended view """
        path = reverse('pages:api_review')
        assert path, APIReviewView.as_view().__name__

    def test_countdown_letters_review(self):
        """ Verify that the `countdown_letters_review` url invokes intended view """
        path = reverse('pages:countdown_letters_review')
        assert path, CountdownLettersReviewView.as_view().__name__

    def test_countdown_numbers_review(self):
        """ Verify that the `countdown_numbers_review` url invokes intended view """
        path = reverse('pages:countdown_numbers_review')
        assert path, CountdownNumbersReviewView.as_view().__name__

    def test_roulette_review(self):
        """ Verify that the `roulette_review` url invokes intended view """
        path = reverse('pages:roulette_review')
        assert path, RouletteReviewView.as_view().__name__

    def test_scraping_review(self):
        """ Verify that the `scraping_review` url invokes intended view """
        path = reverse('pages:scraping_review')
        assert path, ScrapingReviewView.as_view().__name__

    def test_text_analysis_review(self):
        """ Verify that the `text_analysis_review` url invokes intended view """
        path = reverse('pages:text_analysis_review')
        assert path, TextAnalysisReviewView.as_view().__name__

    def test_data_science_review(self):
        """ Verify that the `data_science_review` url invokes intended view """
        path = reverse('pages:data_science_review')
        assert path, DataScienceReviewView.as_view().__name__

    def test_back_end_skills(self):
        """ Verify that the `back_end_skills` url invokes intended view """
        path = reverse('pages:back_end_skills')
        assert path, BackEndSkillsView.as_view().__name__

    def test_front_end_skills(self):
        """ Verify that the `front_end_skills` url invokes intended view """
        path = reverse('pages:front_end_skills')
        assert path, FrontEndSkillsView.as_view().__name__

    def test_infrastructure_skills(self):
        """ Verify that the `infrastructure_skills` url invokes intended view """
        path = reverse('pages:infrastructure_skills')
        assert path, InfrastructureSkillsView.as_view().__name__

    def test_software_skills(self):
        """ Verify that the `software_skills` url invokes intended view """
        path = reverse('pages:software_skills')
        assert path, SoftwareSkillsView.as_view().__name__

    def test_about_me(self):
        """ Verify that the `about_me` url invokes intended view """
        path = reverse('pages:about_me')
        assert path, AboutMeView.as_view().__name__

    def test_privacy(self):
        """ Verify that the `privacy` url invokes intended view """
        path = reverse('pages:privacy')
        assert path, PrivacyPolicyView.as_view().__name__

    def test_reading_list(self):
        """ Verify that the `reading_list` url invokes intended view """
        path = reverse('pages:reading_list')
        assert path, ReadingListView.as_view().__name__
