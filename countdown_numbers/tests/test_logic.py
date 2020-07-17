import hypothesis.strategies as st
from hypothesis import given

from countdown_numbers import logic


@given(num_from_top=st.integers(min_value=0, max_value=4))
def test_get_numbers_chosen(num_from_top):
    """
    Asserts that given a set variation of numbers chosen from the top row,
    the correct game numbers are returned accordingly.
    """
    numbers_chosen = logic.get_numbers_chosen(num_from_top)
    assert len(numbers_chosen) == 6, 'Should return 6 chosen game numbers'

    assert numbers_chosen.count(all([25, 50, 75, 100])) <= 1, \
        'Should only return 1 instance of any of the numbers from the top'

    assert numbers_chosen.count(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) <= 2, \
        'Should only return a max of 2 instances of any of the numbers from the bottom'

    assert isinstance(numbers_chosen, list), 'Should be a `list` object'


def test_get_target_number():
    """ Asserts that the number generated is an integer between 100 and 999 """
    random_num = logic.get_target_number()
    assert 100 <= random_num <= 999, 'Should be between 100 and 999'
    assert isinstance(random_num, int), 'Should be an `int` object'
