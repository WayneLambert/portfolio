from django.urls import path
from scraping import churchill_speech, gettysburg_speech, jokes
from scraping import views as scraping_views

urlpatterns = [
    path('scraping-options/', scraping_views.scraping_options_list,
         name='scraping-options'),
    path('churchill-speech/', churchill_speech.get_churchill_speech,
         name='churchill-speech'),
    path('gettysburg-speech/', gettysburg_speech.get_gettysburg_speech,
         name='gettysburg-speech'),
    path('jokes/', jokes.get_joke, name='jokes'),
]
