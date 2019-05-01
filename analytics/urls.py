from django.urls import path
from analytics.views import AnalyticsViewSet


urlpatterns = [
    path('', AnalyticsViewSet.as_view()),
]
