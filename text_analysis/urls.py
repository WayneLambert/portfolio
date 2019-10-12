from django.urls import path
from text_analysis import views as text_analysis_views

urlpatterns = [
    path('analyse/', text_analysis_views.analyse, name='analyse'),
    path('analysis/', text_analysis_views.analysis, name='analysis'),
]
