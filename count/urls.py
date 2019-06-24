from django.urls import path
from count import views as count_views

urlpatterns = [
    path('check-count/', count_views.check_count, name='check-count'),
    path('count/', count_views.count, name='count'),
]
