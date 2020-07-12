# pylint: disable=redefined-outer-name
import pytest
from django.urls import reverse

from ab_back_end.tests.helpers import lilo_users, user_types
from pages.views import (AboutMeView, APIReviewView, BackEndSkillsView, BlogReviewView,
                         CountdownLettersReviewView, CountdownNumbersReviewView,
                         DataScienceReviewView, FrontEndSkillsView, HomeView,
                         InfrastructureSkillsView, PortfolioView, PrivacyPolicyView,
                         ReadingListView, RouletteReviewView, ScrapingReviewView,
                         SoftwareSkillsView, TextAnalysisReviewView)

pytestmark = pytest.mark.django_db

@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestStaticPagesViews:
    def test_home_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the site's `home` page """
        path = reverse('pages:home')
        request = factory.get(path)
        request.user = lilo_users
        response = HomeView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_portfolio_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `portfolio` page """
        path = reverse('pages:portfolio')
        request = factory.get(path)
        request.user = lilo_users
        response = PortfolioView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_reading_list_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `reading list` page """
        path = reverse('pages:reading_list')
        request = factory.get(path)
        request.user = lilo_users
        response = ReadingListView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_about_me_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `about me` page """
        path = reverse('pages:about_me')
        request = factory.get(path)
        request.user = lilo_users
        response = AboutMeView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_privacy_policy_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the site's `privacy policy` page """
        path = reverse('pages:privacy')
        request = factory.get(path)
        request.user = lilo_users
        response = PrivacyPolicyView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestSkillsPagesViews:
    def test_back_end_skills_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `back end skills` page """
        path = reverse('pages:back_end_skills')
        request = factory.get(path)
        request.user = lilo_users
        response = BackEndSkillsView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_front_end_skills_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `front end skills` page """
        path = reverse('pages:front_end_skills')
        request = factory.get(path)
        request.user = lilo_users
        response = FrontEndSkillsView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_infrastructure_skills_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `infrastructure skills` page """
        path = reverse('pages:infrastructure_skills')
        request = factory.get(path)
        request.user = lilo_users
        response = InfrastructureSkillsView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_software_skills_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the site's `software skills` page """
        path = reverse('pages:software_skills')
        request = factory.get(path)
        request.user = lilo_users
        response = SoftwareSkillsView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'


@pytest.mark.parametrize(argnames='lilo_users', argvalues=lilo_users, ids=user_types)
class TestReviewsPagesViews:
    def test_blog_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `blog review` page """
        path = reverse('pages:blog_review')
        request = factory.get(path)
        request.user = lilo_users
        response = BlogReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_api_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `API review` page """
        path = reverse('pages:api_review')
        request = factory.get(path)
        request.user = lilo_users
        response = APIReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_countdown_letters_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Countdown Letters review` page """
        path = reverse('pages:countdown_letters_review')
        request = factory.get(path)
        request.user = lilo_users
        response = CountdownLettersReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_countdown_numbers_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Countdown Numbers review` page """
        path = reverse('pages:countdown_numbers_review')
        request = factory.get(path)
        request.user = lilo_users
        response = CountdownNumbersReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_roulette_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Roulette review` page """
        path = reverse('pages:roulette_review')
        request = factory.get(path)
        request.user = lilo_users
        response = RouletteReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_scraping_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Scraping review` page """
        path = reverse('pages:scraping_review')
        request = factory.get(path)
        request.user = lilo_users
        response = ScrapingReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_text_analysis_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Text Analysis review` page """
        path = reverse('pages:text_analysis_review')
        request = factory.get(path)
        request.user = lilo_users
        response = TextAnalysisReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'

    def test_data_science_review_view(self, request, factory, lilo_users):
        """ Asserts any user can GET the `Data Science review` page """
        path = reverse('pages:data_science_review')
        request = factory.get(path)
        request.user = lilo_users
        response = DataScienceReviewView.as_view()(request)
        assert response.status_code == 200, 'Should be callable by anyone'
