from django.urls import path

from apps.text_analysis.views import analyse_screen, analysis_screen


app_name = "text_analysis"

urlpatterns = [
    path("analyse/", analyse_screen, name="analyse"),
    path("analysis/", analysis_screen, name="analysis"),
]
