from django.urls import path

from scraping import churchill_speech, gettysburg_speech, referendum
from .views import scraping_options_list

app_name = 'scraping'

urlpatterns = [
    path('scraping-options/', scraping_options_list, name='scraping_options'),
    path('churchill-speech/', churchill_speech.get_churchill_speech, name='churchill_speech'),
    path('gettysburg-speech/',
         gettysburg_speech.get_gettysburg_speech, name='gettysburg_speech'),
    path('referendum/', referendum.get_referendum_results, name='referendum'),
]
