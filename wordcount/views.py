from django.shortcuts import render
from typing import operator
import re


def check_wordcount(request):
    return render(request, 'wordcount/check-wordcount.html')


def count(request):
    word_list = []
    orig_full_text = request.GET['fulltext']
    context = re.sub('[!@#.,/\';]', '', orig_full_text).lower()
    word_list = context.split()
    word_count = len(word_list)

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    context = {
        'orig_full_text': '"' + orig_full_text + '"',
        'context': context,
        'word_count': word_count,
        'sorted_words': sorted_words,
    }

    return render(request, 'wordcount/count.html', context)
