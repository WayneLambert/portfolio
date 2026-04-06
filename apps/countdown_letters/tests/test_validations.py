from apps.countdown_letters import validations


def test_is_eligible_answer(given_answers_list, letters: str = "SVEODRETR"):
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
