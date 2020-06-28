import re
import string
from typing import operator

from django.shortcuts import render

ALPHABET = string.ascii_lowercase

def analyse(request):
    return render(request, 'text_analysis/analyse.html')


def analysis(request):
    word_list = []
    orig_full_text = request.GET['fulltext'].strip()
    cleaned_full_text = re.sub('[!@#.,/\';]', '', orig_full_text).lower()
    word_list = cleaned_full_text.split()
    word_count = len(word_list)

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    def count_char(original_full_text: str, test_char: str) ->int:
        return original_full_text.count(test_char)

    letter_count = []
    if len(letter_count) <= len(cleaned_full_text):
        for test_char in ALPHABET:
            char_count = count_char(cleaned_full_text, test_char)
            perc = 100 * count_char(cleaned_full_text,
                                    test_char) / len(cleaned_full_text)
            letter_count_str = f"{test_char}: {char_count} ({round(perc,1)}%)"
            letter_count.append(letter_count_str.strip('\n'))

    context = {
        'orig_full_text': orig_full_text,
        'cleaned_full_text': cleaned_full_text,
        'word_count': word_count,
        'sorted_words': sorted_words,
        'letter_count': letter_count,
    }

    return render(request, 'text_analysis/analysis.html', context)
