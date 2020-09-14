import pytest

from apps.countdown_letters import validations


@pytest.mark.slow(reason='Processing makes 2 calls to the Oxford Online API')
@pytest.mark.parametrize(argnames='test_word', argvalues=['random', 'radnom'])
@pytest.mark.vcr()
def test_is_in_oxford_api(test_word: str):
    """ Asserts that given a valid word, `True` is returned else `False` """
    in_api = validations.is_in_oxford_api(test_word)
    if test_word == 'random':
        assert in_api
    if test_word == 'radnom':  # Misspelt on purpose
        assert not in_api


def test_is_eligible_answer(given_answers_list, letters: str = 'SVEODRETR'):
    """
    Asserts that given a list fixture containing 8 words, the first 4
    words pass the eligibility tests since all of their letters are
    present and can be used from the game letters. Similarly, the last 4
    items in the list fixture should fail since their letters are not
    present within the game's letters selection.
    """
    answer_eligibility_list = []
    for given_answer in given_answers_list:
        is_eligible_answer = validations.is_eligible_answer(given_answer.upper(), letters)
        answer_eligibility_list.append(is_eligible_answer)

    assert all(answer_eligibility_list[:4])
    assert all(answer_eligibility_list[4:]) != [False, False, False, False]
