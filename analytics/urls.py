from django.urls import path
from analytics.views import AnalyticsViewSet


urlpatterns = [
    path('analytics/', AnalyticsViewSet.as_view(actions={'get': 'list'})),
]
