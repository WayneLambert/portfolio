from django.urls import path
from countdown import views as countdown_views


urlpatterns = [
    path('selection/', countdown_views.render_selection_screen, name='selection'),
    path('game/<int:num_vowels>/', countdown_views.get_letters_selected, name='game'),
    path('results/',
         countdown_views.render_results_screen, name='results'),
]
