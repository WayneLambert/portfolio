import os


def get_words():
    words_list = []
    words_filename = '/Users/waynelambert/Dropbox/Programming/Dev/portfolio/src/countdown/words.txt'
    with open(words_filename, 'r') as words_file:
        for word in words_file:
            words_list.append(word.strip('\n'))

    words = tuple(words_list)
    return words


def get_longest_possible_word(words: tuple, letters: str) -> str:
    """ Returns the longest word in words.txt from the selected letters. """
    cumulative_max_letter_count = 0
    letters_in_selection = list(letters)
    for tested_word in words:
        letters_in_tested_word = list(tested_word.upper())
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = set(letters_in_selection).intersection(
                letters_in_tested_word)
            letter_count = len(common_letters)
            if letter_count > cumulative_max_letter_count:
                if len(tested_word) == len(common_letters):
                    cumulative_max_letter_count = letter_count
                    longest_possible_word = tested_word
    return longest_possible_word.upper()


listed_words = get_words()
letters_chosen = 'NENDOKAXW'
comp_answer = get_longest_possible_word(listed_words, letters_chosen)

end = 'end'
