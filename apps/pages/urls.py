from django.urls import path

from apps.pages.views import (
    APIReviewView,
    BlogReviewView,
    CountdownLettersReviewView,
    CountdownNumbersReviewView,
    DataScienceReviewView,
    PortfolioView,
    PrivacyPolicyView,
    RouletteReviewView,
    ScrapingReviewView,
    SiteHomeView,
    TextAnalysisReviewView,
)


app_name = "pages"

urlpatterns = [
    path("", SiteHomeView.as_view(), name="home"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),
    path("portfolio/reviews/blog/", BlogReviewView.as_view(), name="blog_review"),
    path("portfolio/reviews/api/", APIReviewView.as_view(), name="api_review"),
    path(
        "portfolio/reviews/countdown-letters/",
        CountdownLettersReviewView.as_view(),
        name="countdown_letters_review",
    ),
    path(
        "portfolio/reviews/countdown-numbers/",
        CountdownNumbersReviewView.as_view(),
        name="countdown_numbers_review",
    ),
    path("portfolio/reviews/roulette/", RouletteReviewView.as_view(), name="roulette_review"),
    path("portfolio/reviews/scraping/", ScrapingReviewView.as_view(), name="scraping_review"),
    path(
        "portfolio/reviews/text-analysis/",
        TextAnalysisReviewView.as_view(),
        name="text_analysis_review",
    ),
    path(
        "portfolio/reviews/data-science/",
        DataScienceReviewView.as_view(),
        name="data_science_review",
    ),
    path("privacy/", PrivacyPolicyView.as_view(), name="privacy"),
]
