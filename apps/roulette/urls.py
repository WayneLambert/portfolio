from django.urls import path

from apps.roulette.views import destination_screen, game_screen, view_log_file_contents


app_name = "roulette"

urlpatterns = [
    path("game/", game_screen, name="game"),
    path("destination/", destination_screen, name="destination"),
    path("destination-log-file/", view_log_file_contents, name="log_file"),
]
