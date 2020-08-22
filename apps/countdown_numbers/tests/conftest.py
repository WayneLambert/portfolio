"""
A set of fixtures to facilitate the testing of the Countdown Numbers app
"""

import pytest

from apps.countdown_numbers.forms import SelectedNumbersForm

@pytest.fixture(scope='function')
def selected_numbers_form(request):
    data = {'num_from_top': 0}
    form = SelectedNumbersForm(data=data)
    form.cleaned_data()
    return form
