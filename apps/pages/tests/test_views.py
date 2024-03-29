from django.urls import reverse

import pytest

from apps.pages.views import (
    AboutMeView,
    APIReviewView,
    BackEndSkillsView,
    BadRequestView,
    BlogReviewView,
    CountdownLettersReviewView,
    CountdownNumbersReviewView,
    DataScienceReviewView,
    FrontEndSkillsView,
    InfrastructureSkillsView,
    PageNotFoundView,
    PermissionDeniedView,
    PortfolioView,
    PrivacyPolicyView,
    ReadingListView,
    RouletteReviewView,
    ScrapingReviewView,
    SiteHomeView,
    SoftwareSkillsView,
    TextAnalysisReviewView,
    handler500,
)


pytestmark = pytest.mark.django_db(reset_sequences=True)


@pytest.mark.parametrize(
    argnames="all_users",
    argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
    indirect=True,
)
class TestStaticPagesViews:
    def test_home_view(self, rf, all_users):
        """Asserts any user can GET the site's `home` page"""
        path = reverse("pages:home")
        request = rf.get(path)
        request.user = all_users
        response = SiteHomeView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_portfolio_view(self, rf, all_users):
        """Asserts any user can GET the `portfolio` page"""
        path = reverse("pages:portfolio")
        request = rf.get(path)
        request.user = all_users
        response = PortfolioView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_reading_list_view(self, rf, all_users):
        """Asserts any user can GET the `reading list` page"""
        path = reverse("pages:reading_list")
        request = rf.get(path)
        request.user = all_users
        response = ReadingListView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_about_me_view(self, rf, all_users):
        """Asserts any user can GET the `about me` page"""
        path = reverse("pages:about_me")
        request = rf.get(path)
        request.user = all_users
        response = AboutMeView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_privacy_policy_view(self, rf, all_users):
        """Asserts any user can GET the site's `privacy policy` page"""
        path = reverse("pages:privacy")
        request = rf.get(path)
        request.user = all_users
        response = PrivacyPolicyView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"


@pytest.mark.parametrize(
    argnames="all_users",
    argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
    indirect=True,
)
class TestSkillsPagesViews:
    def test_back_end_skills_view(self, rf, all_users):
        """Asserts any user can GET the `back end skills` page"""
        path = reverse("pages:back_end_skills")
        request = rf.get(path)
        request.user = all_users
        response = BackEndSkillsView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_front_end_skills_view(self, rf, all_users):
        """Asserts any user can GET the `front end skills` page"""
        path = reverse("pages:front_end_skills")
        request = rf.get(path)
        request.user = all_users
        response = FrontEndSkillsView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_infrastructure_skills_view(self, rf, all_users):
        """Asserts any user can GET the `infrastructure skills` page"""
        path = reverse("pages:infrastructure_skills")
        request = rf.get(path)
        request.user = all_users
        response = InfrastructureSkillsView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_software_skills_view(self, rf, all_users):
        """Asserts any user can GET the site's `software skills` page"""
        path = reverse("pages:software_skills")
        request = rf.get(path)
        request.user = all_users
        response = SoftwareSkillsView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"


@pytest.mark.parametrize(
    argnames="all_users",
    argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
    indirect=True,
)
class TestReviewsPagesViews:
    def test_blog_review_view(self, rf, all_users):
        """Asserts any user can GET the `blog review` page"""
        path = reverse("pages:blog_review")
        request = rf.get(path)
        request.user = all_users
        response = BlogReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_api_review_view(self, rf, all_users):
        """Asserts any user can GET the `API review` page"""
        path = reverse("pages:api_review")
        request = rf.get(path)
        request.user = all_users
        response = APIReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_countdown_letters_review_view(self, rf, all_users):
        """Asserts any user can GET the `Countdown Letters review` page"""
        path = reverse("pages:countdown_letters_review")
        request = rf.get(path)
        request.user = all_users
        response = CountdownLettersReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_countdown_numbers_review_view(self, rf, all_users):
        """Asserts any user can GET the `Countdown Numbers review` page"""
        path = reverse("pages:countdown_numbers_review")
        request = rf.get(path)
        request.user = all_users
        response = CountdownNumbersReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_roulette_review_view(self, rf, all_users):
        """Asserts any user can GET the `Roulette review` page"""
        path = reverse("pages:roulette_review")
        request = rf.get(path)
        request.user = all_users
        response = RouletteReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_scraping_review_view(self, request, rf, all_users):
        """Asserts any user can GET the `Scraping review` page"""
        path = reverse("pages:scraping_review")
        request = rf.get(path)
        request.user = all_users
        response = ScrapingReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_text_analysis_review_view(self, rf, all_users):
        """Asserts any user can GET the `Text Analysis review` page"""
        path = reverse("pages:text_analysis_review")
        request = rf.get(path)
        request.user = all_users
        response = TextAnalysisReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"

    def test_data_science_review_view(self, rf, all_users):
        """Asserts any user can GET the `Data Science review` page"""
        path = reverse("pages:data_science_review")
        request = rf.get(path)
        request.user = all_users
        response = DataScienceReviewView.as_view()(request)
        assert response.status_code == 200, "Should be callable by anyone"


class TestCustomErrorPages:
    @pytest.mark.parametrize(
        argnames="all_users",
        argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
        indirect=True,
    )
    def test_400_page(self, rf, all_users):
        """Asserts a user can GET a 400 page"""
        path = reverse("pages:home")
        request = rf.get(path)
        request.user = all_users
        response = BadRequestView.as_view()(request)
        assert response.status_code == 200, "the custom 400 template should GET `OK` response"

    def test_403_page(self, rf, pub_post, auth_user):
        """Asserts a user can GET a 403 page"""
        kwargs = {"slug": pub_post.slug}
        path = reverse("blog:post_update", kwargs=kwargs)
        request = rf.get(path)
        request.user = auth_user
        response = PermissionDeniedView.as_view()(request)
        assert response.status_code == 200, "the custom 403 template should GET an `OK` response"

    @pytest.mark.parametrize(
        argnames="all_users",
        argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
        indirect=True,
    )
    def test_404_page(self, rf, all_users):
        """Asserts a user can GET a 404 page"""
        kwargs = {"slug": "post-slug-that-does-not-exist"}
        path = reverse("blog:post_update", kwargs=kwargs)
        request = rf.get(path)
        request.user = all_users
        response = PageNotFoundView.as_view()(request)
        assert response.status_code == 200, "the custom 404 template should GET `OK` response"

    @pytest.mark.parametrize(
        argnames="all_users",
        argvalues=[pytest.param("auth_user"), pytest.param("unauth_user")],
        indirect=True,
    )
    def test_500_page(self, rf, all_users):
        """Asserts a user can GET a 500 page"""
        path = reverse("pages:home")
        request = rf.get(path)
        request.user = all_users
        response = handler500(request)
        assert response.status_code == 500, "the user should GET a 500 status code"
