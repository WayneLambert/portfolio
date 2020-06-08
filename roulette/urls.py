from django.urls import path
from roulette import views as roulette_views


app_name = 'roulette'

urlpatterns = [
    path('game/', roulette_views.game_screen, name='holiday_roulette'),
    path('destination/', roulette_views.destination_screen, name='holiday_destination'),
    path('destination-log-file/',
         roulette_views.view_log_file_contents, name='destination_log_file'),
]
