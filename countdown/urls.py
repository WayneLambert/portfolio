from django.urls import path
from countdown import views as countdown_views


urlpatterns = [
    path('selection/', countdown_views.selection_screen, name='selection'),
    path('game/', countdown_views.game_screen, name='game'),
    path('results/', countdown_views.results_screen, name='results'),
]
