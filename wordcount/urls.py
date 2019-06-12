from django.urls import path
from wordcount import views as wordcount_views

urlpatterns = [
    path('check-wordcount/', wordcount_views.check_wordcount, name='check-wordcount'),
    path('count/', wordcount_views.count, name='count'),
]
