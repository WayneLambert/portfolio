from django.urls import path

from scraping import churchill_speech, gettysburg_speech, jokes, referendum
from scraping import views as scraping_views

app_name = 'scraping'

urlpatterns = [
    path('scraping-options/', scraping_views.scraping_options_list, name='scraping_options'),
    path('churchill-speech/', churchill_speech.get_churchill_speech, name='churchill_speech'),
    path('gettysburg-speech/',
         gettysburg_speech.get_gettysburg_speech, name='gettysburg_speech'),
    path('jokes/', jokes.get_joke, name='jokes'),
    path('referendum/', referendum.get_referendum_results, name='referendum'),
]
