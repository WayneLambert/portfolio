from django.urls import path

from apps.scraping.churchill import get_churchill_speech
from apps.scraping.gettysburg import get_gettysburg_speech
from apps.scraping.referendum import get_referendum_results
from apps.scraping.views import ScrapingOptionsView


app_name = 'scraping'

urlpatterns = [
    path('scraping-options/', ScrapingOptionsView.as_view(), name='scraping_options'),
    path('churchill-speech/', get_churchill_speech, name='churchill_speech'),
    path('gettysburg-speech/', get_gettysburg_speech, name='gettysburg_speech'),
    path('eu-referendum-results/', get_referendum_results, name='referendum'),
]
