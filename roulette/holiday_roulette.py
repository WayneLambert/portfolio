"""
This code is for the procrastinating traveller that just can't decide where they
should go to next. There is a sleep of 1 second between each choice made by the
random selection so the traveller can watch the logging on the screen as if it
is a roulette wheel that decides their fate.

Increase the level of time.sleep() for the additional suspense factor. :)
"""

import operator
import random
import time
from logging import DEBUG, basicConfig, debug

log_file = 'roulette/holiday_roulette.log'

# Detailed logging example below...
basicConfig(
    filename=log_file,
    level=DEBUG,
    format="""%(asctime)s.%(msecs)03d %(levelname)-8s %(filename)s:
        %(module)s: %(lineno)d - %(funcName)s: %(message)s""",
    datefmt="%Y-%m-%d %H:%M:%S")

places_to_go = {
    'Barbados': 0,
    'Koh Samui': 0,
    'Langkawi': 0,
    'Seychelles': 0,
    'Hawaii': 0,
    'Bora Bora': 0,
    'Fiji': 0,
    'St. Lucia': 0,
    'Aruba': 0,
    'Santorini': 0,
    'Palawan': 0,
    'Maldives': 0,
}

def get_place_to_go():
    num_of_choices = 500
    for place_selected in range(1, num_of_choices + 1):
        time.sleep(0.1)
        choice_num = random.randint(0, len(places_to_go) - 1)
        choice = list(places_to_go.keys())[choice_num]
        places_to_go[choice] += 1
        debug(f'Choice #{place_selected} was {choice}')
        print(f'Choice #{place_selected} was {choice}')
    most_selected_place = max(places_to_go.items(), key=operator.itemgetter(1))[0]
    number_of_times_selected = max(places_to_go.items(), key=operator.itemgetter(1))[1]
    return (most_selected_place, number_of_times_selected)


# Code to clear down existing log file here
if __name__ == '__main__':
    with open(log_file, 'w'):
        pass
    chosen_place = get_place_to_go()
    print(f'The chosen place to visit was {chosen_place[0]} with {chosen_place[1]} selections.')
