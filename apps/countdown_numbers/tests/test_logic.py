import hypothesis.strategies as st
import pytest

from hypothesis import given

from apps.countdown_numbers import logic


@given(num_from_top=st.integers(min_value=0, max_value=4))
def test_get_numbers_chosen(num_from_top):
    """
    Asserts that given a set variation of numbers chosen from the top
    row, the correct game numbers are returned accordingly.
    """
    numbers_chosen = logic.get_numbers_chosen(num_from_top)
    assert len(numbers_chosen) == 6, 'Should return 6 chosen game numbers'

    assert numbers_chosen.count(all([25, 50, 75, 100])) <= 1, \
        'Should only return 1 instance of any of the numbers from the top'

    assert numbers_chosen.count(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) <= 2, \
        'Should only return a max of 2 instances of any of the numbers from the bottom'

    assert isinstance(numbers_chosen, list), 'Should be a `list` object'


def test_get_target_number():
    """
    Asserts that the number generated is an integer between 100 and 999
    """
    random_num = logic.get_target_number()
    assert 100 <= random_num <= 999, 'Should be between 100 and 999'
    assert isinstance(random_num, int), 'Should be an `int` object'


@pytest.mark.parametrize(argnames='num_from_top', argvalues=[0, 1, 2, 3, 4])
def test_build_game_url(num_from_top):
    """ Asserts that the correct game URL is built """
    game_url = logic.build_game_url(num_from_top)
    assert '/countdown-numbers/game/?target_number=' in game_url
    assert '&numbers_chosen=' in game_url
    assert isinstance(game_url, str)


@given(target_number=st.integers(min_value=100, max_value=999))
def test_score_awarded_for_achieving_target_number(target_number):
    """
    Asserts that given a variation of target numbers, 10 points is
    awarded for achieving the target number.
    """
    num_achieved = target_number
    score_awarded = logic.get_score_awarded(target_number, num_achieved)
    assert score_awarded == 10, 'Should be 10 points for achieving the target number'


@given(num_achieved_var=st.integers(min_value=-5, max_value=5).filter(lambda x: x != 0))
def test_score_awarded_for_being_within_5_of_target_number(num_achieved_var):
    """
    Asserts that a player is awarded 7 points for being within a
    variance of 1-5 either side of the target number.
    """
    TARGET_NUMBER = 500
    num_achieved = TARGET_NUMBER + num_achieved_var
    score_awarded = logic.get_score_awarded(TARGET_NUMBER, num_achieved)
    assert score_awarded == 7, 'Should score 7 points for being within 1-5 either side'


@given(num_achieved_var=st.integers(min_value=-10, max_value=10).filter(lambda x: not -5 <= x <= 5))
def test_score_awarded_for_being_within_10_of_target_number(num_achieved_var):
    """
    Asserts that a player is awarded 5 points for being within a
    variance of 6-10 either side of the target number.
    """
    TARGET_NUMBER = 500
    num_achieved = TARGET_NUMBER + num_achieved_var
    score_awarded = logic.get_score_awarded(TARGET_NUMBER, num_achieved)
    assert score_awarded == 5, 'Should score 5 points for being within 6-10 either side'


@given(num_achieved_var=st.integers(min_value=-400, max_value=499).filter(lambda x: not -10 <= x <= 10))
def test_score_awarded_for_being_more_than_10_away_from_target_number(num_achieved_var):
    """
    Asserts that a player is awarded zero points for being more than 10
    either side of the target number.
    """
    TARGET_NUMBER = 500
    num_achieved = TARGET_NUMBER + num_achieved_var
    score_awarded = logic.get_score_awarded(TARGET_NUMBER, num_achieved)
    assert score_awarded == 0, 'Should score 0 points for being more than 10 away either side'


def test_get_game_result_is_draw_1():
    """
    Asserts the game result is a `draw` when both player's achieve the
    target number.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 500,
        'player_num_achieved': 500,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Draw'


def test_get_game_result_is_draw_2():
    """
    Asserts the game result is a `draw` when both player's have the same
    variance above the target number.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 505,
        'player_num_achieved': 505,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Draw'


def test_get_game_result_is_draw_3():
    """
    Asserts the game result is a `draw` when both player's have the same
    variance below the target number.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 495,
        'player_num_achieved': 495,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Draw'


def test_get_game_result_is_draw_4():
    """
    Asserts the game result is a `draw` when both player's have the same
    variance from the target number but in opposite directions.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 495,
        'player_num_achieved': 505,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Draw'


def test_rachel_wins_when_closer_but_above_target_number():
    """
    Asserts that the correct game result is given when both player's are
    the same distance from the target number but in different directions.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 501,
        'player_num_achieved': 502,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Rachel wins'


def test_rachel_wins_when_closer_but_below_target_number():
    """
    Asserts that the correct game result is given when both player's are
    the same distance from the target number but in different directions.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 499,
        'player_num_achieved': 498,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Rachel wins'


def test_player_wins_when_closer_but_above_target_number():
    """
    Asserts that the correct game result is given when both player's are
    the same distance from the target number but in different directions.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 502,
        'player_num_achieved': 501,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Player wins'


def test_player_wins_when_closer_but_below_target_number():
    """
    Asserts that the correct game result is given when both player's are
    the same distance from the target number but in different directions.
    """
    TARGET_NUMBER = 500
    answers = {
        'comp_num_achieved': 498,
        'player_num_achieved': 499,
    }
    game_result = logic.get_game_result(TARGET_NUMBER, answers)
    assert game_result == 'Player wins'
