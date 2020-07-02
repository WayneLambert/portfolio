import string
from collections import defaultdict
from decimal import Decimal

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_area_results(results: dict) ->list:
    area_results = zip(
        results['area_name'],
        results['leave_votes'],
        results['leave_percent'],
        results['remain_votes'],
        results['remain_percent'],
        results['area_votes'],
        results['turnout'],
    )
    results = []
    for area in area_results:
        results.append(area)

    return results

def get_referendum_results(request):
    """
    Retrieves the 2016 Brexit Referendum results from the BBC website.
    """
    ALPHABET = string.ascii_lowercase
    BASE_URL = 'https://www.bbc.co.uk/news/politics/eu_referendum/results/local/'
    results = defaultdict(list)
    leave_votes, remain_votes = 0, 0
    for letter in ALPHABET:
        page_response = requests.get(f"{BASE_URL}{letter}", timeout=5)
        if page_response:
            page_content = BeautifulSoup(page_response.content, "html.parser")
            areas = page_content.find_all('div', attrs={'class': 'eu-ref-result-bar'})
            for area in areas:
                results['area_name'].append(area.find('h3').getText())
                cleaned_leave_votes = int(area.find_all('div',
                                                        {'class': 'eu-ref-result-bar__votes'}
                                                        )[0].string.strip().split('\n')
                                          [0].strip().replace(',', ''))
                results['leave_votes'].append(cleaned_leave_votes)
                cleaned_remain_votes = int(area.find_all('div',
                                                         {'class': 'eu-ref-result-bar__votes'}
                                                        )[1].string.strip().split('\n')
                                           [0].strip().replace(',', ''))
                results['remain_votes'].append(cleaned_remain_votes)
                area_votes = cleaned_leave_votes + cleaned_remain_votes
                results['area_votes'].append(area_votes)
                results['leave_percent'].append(f"{cleaned_leave_votes / area_votes:.1%}")
                results['remain_percent'].append(f"{cleaned_remain_votes / area_votes:.1%}")
                results['turnout'].append(area.find(
                    'div', {'class': 'eu-ref-result-bar__turnout'})
                                          .getText().replace('Turnout: ', '')
                                          )
                leave_votes = sum(Decimal(num) for num in results['leave_votes'])
                remain_votes = sum(Decimal(num) for num in results['remain_votes'])
                total_votes = leave_votes + remain_votes
                total_leave_percent = f"{leave_votes / total_votes:.1%}"
                total_remain_percent = f"{remain_votes / total_votes:.1%}"
        else:
            continue
    results = get_area_results(dict(results))


    context = {
        'results': results,
        'leave_votes': leave_votes,
        'remain_votes': remain_votes,
        'area_votes': area_votes,
        'total_votes': total_votes,
        'total_leave_percent': total_leave_percent,
        'total_remain_percent': total_remain_percent,
    }

    return render(request, 'referendum.html', {'context': context})
