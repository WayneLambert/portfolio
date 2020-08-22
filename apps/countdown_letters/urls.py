from django.urls import path

from apps.countdown_letters.views import game_screen, results_screen, selection_screen


app_name = 'countdown_letters'

urlpatterns = [
    path('selection/', selection_screen, name='selection'),
    path('game/', game_screen, name='game'),
    path('results/', results_screen, name='results'),
]
