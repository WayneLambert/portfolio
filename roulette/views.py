from django.shortcuts import render

from .logic import (clear_down_log_file, get_picture_url, get_roulette_result,
                    read_log_file, reset_places_to_go)


def game_screen(request):
    clear_down_log_file(request)
    return render(request, 'roulette/game.html')


def destination_screen(request):
    reset_places_to_go(request)
    clear_down_log_file(request)
    roulette_result = get_roulette_result(request)
    destination_image_url = get_picture_url(roulette_result[1])
    context = {
        'places_to_go': roulette_result[0],
        'most_selected_place': roulette_result[1],
        'number_of_times_selected': roulette_result[2],
        'detailed_choices': roulette_result[3],
        'destination_image_url': destination_image_url,
    }

    return render(request, 'roulette/destination.html', context)


def view_log_file_contents(request):
    context = {'log_file_contents': read_log_file(request)}
    return render(request, 'roulette/log_file_contents.html', context)
