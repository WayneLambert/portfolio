from django.urls import path

from .views import (AboutMeView, APIReviewView, BackEndSkillsView, BlogReviewView,
                    FrontEndSkillsView, HomeView, InfrastructureSkillsView, PortfolioView,
                    PrivacyPolicyView, ReadingListView, SoftwareSkillsView)

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/reviews/blog/', BlogReviewView.as_view(), name='blog_review'),
    path('portfolio/reviews/api/', APIReviewView.as_view(), name='api_review'),
    path('skills/back-end/', BackEndSkillsView.as_view(), name='back_end_skills'),
    path('skills/front-end/', FrontEndSkillsView.as_view(), name='front_end_skills'),
    path('skills/infrastructure/',
         InfrastructureSkillsView.as_view(), name='infrastructure_skills'),
    path('skills/software/', SoftwareSkillsView.as_view(), name='software_skills'),
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('reading-list/', ReadingListView.as_view(), name='reading_list'),
]
