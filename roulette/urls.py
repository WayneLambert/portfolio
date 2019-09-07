from django.urls import path
from roulette import views as roulette_views


urlpatterns = [
    path('game/', roulette_views.game_screen, name='holiday-roulette'),
    path('destination/', roulette_views.destination_screen, name='holiday-destination'),
    path('destination-log-file/', roulette_views.view_log_file_contents,
         name='destination-log-file'),
]
