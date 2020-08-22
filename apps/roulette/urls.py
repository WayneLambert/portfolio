from django.urls import path

from apps.roulette.views import destination_screen, game_screen, view_log_file_contents

app_name = 'roulette'

urlpatterns = [
    path('game/', game_screen, name='holiday_roulette'),
    path('destination/', destination_screen, name='holiday_destination'),
    path('destination-log-file/', view_log_file_contents, name='destination_log_file'),
]
