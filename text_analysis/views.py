from django.shortcuts import render

from .utils import (get_cleaned_full_text, get_letter_counts, get_orig_full_text,
                    get_sorted_words, get_word_list)


def analyse_screen(request):
    return render(request, 'text_analysis/analyse.html')


def analysis_screen(request):
    cleaned_full_text = get_cleaned_full_text(request)
    word_list = get_word_list(cleaned_full_text)

    context = {
        'orig_full_text': get_orig_full_text(request),
        'cleaned_full_text': cleaned_full_text,
        'word_count': len(word_list),
        'sorted_words': get_sorted_words(word_list),
        'letter_count': get_letter_counts(cleaned_full_text),
    }

    return render(request, 'text_analysis/analysis.html', context)
