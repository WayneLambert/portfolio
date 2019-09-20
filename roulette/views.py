import operator
import random
import time
from logging import DEBUG, basicConfig, debug
from django.shortcuts import render

BASE_LOC = 'https://wl-portfolio.s3.eu-west-2.amazonaws.com/post_images/holiday-roulette/'
log_file = 'roulette/holiday_roulette.log'

# Detailed logging example below...
basicConfig(
    filename=log_file,
    level=DEBUG,
    format="""%(asctime)s.%(msecs)03d %(levelname)-8s %(filename)s:
        %(module)s: %(lineno)d - %(funcName)s: %(message)s""",
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


def get_roulette_result(request):
    num_of_choices = 1000
    detailed_choices = []
    for place_selected in range(1, num_of_choices + 1):
        time.sleep(0.005)
        choice_num = random.randint(0, len(places_to_go) - 1)
        choice = list(places_to_go.keys())[choice_num]
        places_to_go[choice] += 1
        choice_item = f'Choice #{place_selected} was {choice}'
        debug(choice_item)
        print(choice_item)
        detailed_choices.append(choice_item)
    most_selected_place = max(places_to_go.items(),
                              key=operator.itemgetter(1))[0]
    number_of_times_selected = max(
        places_to_go.items(), key=operator.itemgetter(1))[1]
    return (
        places_to_go,
        most_selected_place,
        number_of_times_selected,
        detailed_choices
    )


def get_picture_url(destination):
    locations = {
        'Aruba': f"{BASE_LOC}{'aruba.jpg'}",
        'Barbados': f"{BASE_LOC}{'barbados.jpg'}",
        'Bora Bora': f"{BASE_LOC}{'bora-bora.jpg'}",
        'Fiji': f"{BASE_LOC}{'fiji.jpg'}",
        'Hawaii': f"{BASE_LOC}{'hawaii.jpg'}",
        'Koh Samui': f"{BASE_LOC}{'koh-samui.jpg'}",
        'Langkawi': f"{BASE_LOC}{'langkawi.jpg'}",
        'Maldives': f"{BASE_LOC}{'maldives.jpg'}",
        'Palawan': f"{BASE_LOC}{'palawan.jpg'}",
        'Santorini': f"{BASE_LOC}{'santorini.jpg'}",
        'Seychelles': f"{BASE_LOC}{'seychelles.jpg'}",
        'St. Lucia': f"{BASE_LOC}{'st-lucia.jpg'}",
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


def read_log_file(request):
    with open(log_file, 'r') as file:
        contents = []
        for line in file.readlines():
            contents.append(line)
        return contents


def view_log_file_contents(request):
    log_file_contents = read_log_file(request)
    context = {
        'log_file_contents': log_file_contents,
    }
    return render(request, 'roulette/log_file_contents.html', context)
