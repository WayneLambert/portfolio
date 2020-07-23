from django.shortcuts import render

from . import logic


def game_screen(request):
    logic.clear_down_log_file()
    return render(request, 'roulette/game.html')


def destination_screen(request):
    logic.reset_places_to_go()
    logic.clear_down_log_file()
    roulette_result = logic.get_roulette_result()
    destination_image_url = logic.get_picture_url(roulette_result[1])
    context = {
        'places_to_go': roulette_result[0],
        'most_selected_place': roulette_result[1],
        'number_of_times_selected': roulette_result[2],
        'detailed_choices': roulette_result[3],
        'destination_image_url': destination_image_url,
    }

    return render(request, 'roulette/destination.html', context)


def view_log_file_contents(request):
    context = {'log_file_contents': logic.read_log_file()}
    return render(request, 'roulette/log_file_contents.html', context)
