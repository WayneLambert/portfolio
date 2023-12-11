import string

from collections import defaultdict
from typing import Any, List, Tuple

from django.shortcuts import render

import requests

from bs4 import BeautifulSoup


class ScrapingError(Exception):
    """
    The content could not be scraped from the BBC website. Perhaps the
    website is down.
    """


def get_area_results(results: dict) -> List[Tuple[Any]]:
    """Assembles each area's results into an iterable for rendering"""
    area_results = zip(
        results["area_name"],
        results["leave_votes"],
        results["leave_percent"],
        results["remain_votes"],
        results["remain_percent"],
        results["area_votes"],
        results["turnout"],
    )
    results = list(area_results)
    return results


def scrape_content() -> List[List[int]]:
    """Scrapes the results of the EU Referendum from the BBC website"""
    ALPHABET = string.ascii_lowercase
    BASE_URL = "https://www.bbc.co.uk/news/politics/eu_referendum/results/local/"
    results = defaultdict(list)
    for letter in ALPHABET:
        page_response = requests.get(f"{BASE_URL}{letter}", timeout=5)
        try:
            page_content = BeautifulSoup(page_response.content, "html.parser")
            areas = page_content.find_all("div", attrs={"class": "eu-ref-result-bar"})
            for area in areas:
                results["area_name"].append(area.find("h3").getText())
                cleaned_leave_votes = int(
                    area.find_all("div", {"class": "eu-ref-result-bar__votes"})[0]
                    .string.strip()
                    .split("\n")[0]
                    .strip()
                    .replace(",", "")
                )
                results["leave_votes"].append(cleaned_leave_votes)
                cleaned_remain_votes = int(
                    area.find_all("div", {"class": "eu-ref-result-bar__votes"})[1]
                    .string.strip()
                    .split("\n")[0]
                    .strip()
                    .replace(",", "")
                )
                results["remain_votes"].append(cleaned_remain_votes)
                area_votes = cleaned_leave_votes + cleaned_remain_votes
                results["area_votes"].append(area_votes)
                results["leave_percent"].append(f"{cleaned_leave_votes / area_votes:.1%}")
                results["remain_percent"].append(f"{cleaned_remain_votes / area_votes:.1%}")
                results["turnout"].append(
                    area.find("div", {"class": "eu-ref-result-bar__turnout"})
                    .getText()
                    .replace("Turnout: ", "")
                )
        except:  # pragma: no cover
            raise ScrapingError

    return results


def calc_leave_votes(results: list) -> int:
    """Calculates total number of leave votes from scraped data"""
    return sum(result[1] for result in results)


def calc_remain_votes(results: list) -> int:
    """Calculates total number of remain votes from scraped data"""
    return sum(result[3] for result in results)


def get_referendum_results(request):
    """Retrieves 2016 Brexit Referendum results from BBC website"""
    results = scrape_content()
    results = get_area_results(dict(results))
    leave_votes = calc_leave_votes(results)
    remain_votes = calc_remain_votes(results)
    total_votes = leave_votes + remain_votes
    total_leave_percent = f"{leave_votes / total_votes:.1%}"
    total_remain_percent = f"{remain_votes / total_votes:.1%}"

    context = {
        "results": results,
        "leave_votes": leave_votes,
        "remain_votes": remain_votes,
        "total_votes": total_votes,
        "total_leave_percent": total_leave_percent,
        "total_remain_percent": total_remain_percent,
    }

    return render(request, "referendum.html", {"context": context})
