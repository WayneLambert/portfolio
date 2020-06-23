import operator
import random
import os
import time
import logging

from django.conf import settings
from django.shortcuts import render

log_file = os.path.join(settings.BASE_DIR, 'roulette/holiday_roulette.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="""%(asctime)s.%(msecs)03d %(levelname)-8s %(filename)s %(module)s: %(lineno)d - %(funcName)s: %(message)s""",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def clear_down_log_file(request):
    with open(log_file, 'w'):
        pass


def game_screen(request):
    clear_down_log_file(request)
    return render(request, 'roulette/game.html')


places_to_go = {
    'Aruba': 0,
    'Barbados': 0,
    'Bora Bora': 0,
    'Fiji': 0,
    'Hawaii': 0,
    'Koh Samui': 0,
    'Langkawi': 0,
    'Maldives': 0,
    'Palawan': 0,
    'Santorini': 0,
    'Seychelles': 0,
    'St. Lucia': 0,
}


def reset_places_to_go(request):
    for key in places_to_go:
        places_to_go[key] = 0


def get_roulette_result(request) ->tuple:
    num_of_choices = 1000
    detailed_choices = []
    for place_selected in range(1, num_of_choices + 1):
        time.sleep(0.003)
        choice_num = random.randint(0, len(places_to_go) - 1)
        choice = list(places_to_go.keys())[choice_num]
        places_to_go[choice] += 1
        choice_item = f"Choice #{place_selected} was {choice}"
        logging.info(choice_item)
        print(choice_item)
        detailed_choices.append(choice_item)
    most_selected_place = max(places_to_go.items(), key=operator.itemgetter(1))[0]
    number_of_times_selected = max(places_to_go.items(), key=operator.itemgetter(1))[1]
    return (places_to_go, most_selected_place, number_of_times_selected, detailed_choices)


def get_picture_url(destination: str) ->str:
    AWS_FOLDER = f"{settings.AWS_BASE_BUCKET_ADDRESS}/post_images/holiday-roulette/"
    locations = {
        'Aruba': f"{AWS_FOLDER}aruba.jpg",
        'Barbados': f"{AWS_FOLDER}barbados.jpg",
        'Bora Bora': f"{AWS_FOLDER}bora-bora.jpg",
        'Fiji': f"{AWS_FOLDER}fiji.jpg",
        'Hawaii': f"{AWS_FOLDER}hawaii.jpg",
        'Koh Samui': f"{AWS_FOLDER}koh-samui.jpg",
        'Langkawi': f"{AWS_FOLDER}langkawi.jpg",
        'Maldives': f"{AWS_FOLDER}maldives.jpg",
        'Palawan': f"{AWS_FOLDER}palawan.jpg",
        'Santorini': f"{AWS_FOLDER}santorini.jpg",
        'Seychelles': f"{AWS_FOLDER}seychelles.jpg",
        'St. Lucia': f"{AWS_FOLDER}st-lucia.jpg",
    }
    return locations.get(destination, "Invalid destination")


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


def read_log_file(request) ->list:
    with open(log_file, 'r') as file:
        contents = []
        for line in file.readlines():
            contents.append(line)
        return contents


def view_log_file_contents(request):
    context = {'log_file_contents': read_log_file(request)}
    return render(request, 'roulette/log_file_contents.html', context)
