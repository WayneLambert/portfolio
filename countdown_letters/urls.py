from django.urls import path
from countdown_letters import views as countdown_letters_views

app_name = 'countdown-letters'

urlpatterns = [
    path('selection/', countdown_letters_views.selection_screen, name='selection'),
    path('game/', countdown_letters_views.game_screen, name='game'),
    path('results/', countdown_letters_views.results_screen, name='results'),
]
