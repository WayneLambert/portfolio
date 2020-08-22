from django.shortcuts import render

from apps.text_analysis import utils


def analyse_screen(request):
    return render(request, 'text_analysis/analyse.html')


def analysis_screen(request):
    cleaned_full_text = utils.get_cleaned_full_text(request)
    word_list = utils.get_word_list(cleaned_full_text)

    context = {
        'orig_full_text': utils.get_orig_full_text(request),
        'cleaned_full_text': cleaned_full_text,
        'word_count': len(word_list),
        'sorted_words': utils.get_sorted_words(word_list),
        'letter_count': utils.get_letter_counts(cleaned_full_text),
    }

    return render(request, 'text_analysis/analysis.html', context)
