from django.urls import path

from .views import (AboutMeView, BlogReviewView, DevSkillsView, HomeView, PortfolioView,
                    PrivacyPolicyView, ReadingListView)

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/reviews/blog/', BlogReviewView.as_view(), name='blog_review'),
    path('skills/back-end/', DevSkillsView.as_view(), name='back_end_skills'),
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('reading-list/', ReadingListView.as_view(), name='reading_list'),
]
