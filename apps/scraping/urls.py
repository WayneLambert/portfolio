from django.urls import path

from scraping.referendum import get_referendum_results
from scraping.views import ScrapingOptionsView


app_name = "scraping"

urlpatterns = [
    path("scraping-options/", ScrapingOptionsView.as_view(), name="scraping_options"),
    path("eu-referendum-results/", get_referendum_results, name="referendum"),
]
