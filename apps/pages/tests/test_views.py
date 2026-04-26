from django.urls import reverse

import pytest

from pages.views import (
    BadRequestView,
    handler500,
    PageNotFoundView,
    PermissionDeniedView,
    PortfolioView,
    SiteHomeView,
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
