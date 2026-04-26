from django.urls import path

from pages.views import (
    PortfolioView,
    SiteHomeView,
)


app_name = "pages"

urlpatterns = [
    path("", SiteHomeView.as_view(), name="home"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
]
