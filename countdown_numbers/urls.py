from django.urls import path

from .views import game_screen, results_screen, selection_screen

app_name = 'countdown_numbers'

urlpatterns = [
    path('selection/', selection_screen, name='selection'),
    path('game/', game_screen, name='game'),
    path('results/', results_screen, name='results'),
]
