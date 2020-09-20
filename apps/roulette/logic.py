import logging
import operator
import random
import time

from typing import Tuple

from django.conf import settings

from apps.roulette.logging import log_file


class Game:
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


def clear_down_log_file():
    """ Clears down the contents of the log file """
    with open(log_file, 'w'):
        pass


def reset_places_to_go():
    """ Resets the dictionary count to zero for each destination """
    for key in Game.places_to_go:
        Game.places_to_go[key] = 0


def get_roulette_result() -> Tuple[dict, str, int, list]:
    """
    Gets the result of the roulette game and introduces suspense in
    the game due to a time.sleep() function.
    """
    num_of_choices = 1000
    detailed_choices = []
    for place_selected in range(1, num_of_choices + 1):
        time.sleep(0.003)
        choice_num = random.randint(0, len(Game.places_to_go) - 1)
        choice = list(Game.places_to_go.keys())[choice_num]
        Game.places_to_go[choice] += 1
        choice_item = f"Choice #{place_selected} was {choice}"
        logging.info(choice_item)
        detailed_choices.append(choice_item)
    most_selected_place = max(Game.places_to_go.items(), key=operator.itemgetter(1))[0]
    number_of_times_selected = max(Game.places_to_go.items(), key=operator.itemgetter(1))[1]
    return (Game.places_to_go, most_selected_place, number_of_times_selected, detailed_choices)


def get_picture_url(destination: str) -> str:
    """ Builds the URL for the destinations' image from an S3 bucket """
    aws_folder = f"{settings.AWS_BASE_BUCKET_ADDRESS}/post_images/holiday-roulette/"
    locations = {
        'Aruba': f"{aws_folder}aruba.jpg",
        'Barbados': f"{aws_folder}barbados.jpg",
        'Bora Bora': f"{aws_folder}bora-bora.jpg",
        'Fiji': f"{aws_folder}fiji.jpg",
        'Hawaii': f"{aws_folder}hawaii.jpg",
        'Koh Samui': f"{aws_folder}koh-samui.jpg",
        'Langkawi': f"{aws_folder}langkawi.jpg",
        'Maldives': f"{aws_folder}maldives.jpg",
        'Palawan': f"{aws_folder}palawan.jpg",
        'Santorini': f"{aws_folder}santorini.jpg",
        'Seychelles': f"{aws_folder}seychelles.jpg",
        'St. Lucia': f"{aws_folder}st-lucia.jpg",
    }
    return locations.get(destination, "Invalid destination")


def read_log_file() -> list:
    """ Reads log file to a list for later rendering to results page """
    with open(log_file, 'r') as file:
        contents = []
        for line in file.readlines():  # pragma: no cover
            contents.append(line)
        return contents
