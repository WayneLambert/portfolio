from django.urls import path
from scraping import churchill_speech, gettysburg_speech
from scraping import views as scraping_views

urlpatterns = [
    path('speech-list/', scraping_views.speech_list, name='speech-list'),
    path('churchill-speech/', churchill_speech.get_churchill_speech,
         name='churchill-speech'),
    path('gettysburg-speech/', gettysburg_speech.get_gettysburg_speech,
         name='gettysburg-speech'),
]
