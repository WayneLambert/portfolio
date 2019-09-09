from django.urls import path
from countdown_numbers import views as countdown_numbers_views

app_name = 'countdown-numbers'
urlpatterns = [
    path('selection/', countdown_numbers_views.selection_screen, name='selection'),
    path('game/', countdown_numbers_views.game_screen, name='game'),
    # path('results/', countdown_numbers_views.results_screen, name='results'),
]
