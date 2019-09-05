""" Calculates the number of `guesses` required to arrive at the `chosen_num` """

import array

def binary_search(tmp_array, guess):
    guess_count = 1
    lower_bound = 0
    upper_bound = len(tmp_array)

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2

        if guess < midpoint:
            upper_bound = midpoint - 1
            guess_count += 1
        elif guess > midpoint:
            lower_bound = midpoint + 1
            guess_count += 1
        elif guess == midpoint:
            return guess_count


if __name__ == '__main__':
    million_item_array = array.array('i', (i for i in range(1, 1000001)))
    chosen_num = 646234

    number_of_guesses = binary_search(million_item_array, chosen_num)

    print(f'It took {number_of_guesses} guesses to get to the right number.')
