from django.urls import path

from .views import AboutMeView, HomeView, PortfolioView, PrivacyPolicyView, ReadingListView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('reading-list/', ReadingListView.as_view(), name='reading_list'),
]
