from django.urls import path

from .views import (AboutMeView, ContactView, CVView, HomeView, PortfolioView,
                    PrivacyPolicyView, ReadingListView)

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('cv', CVView.as_view(), name='cv'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about-me/', AboutMeView.as_view(), 'about_me'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), 'privacy_policy'),
    path('reading-list/', ReadingListView.as_view(), 'reading_list'),
]
