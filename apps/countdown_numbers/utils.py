""" Fnctions not associated with core game logic or validations. """

from apps.countdown_numbers.models import NumbersGame


def create_record(context: dict):
    """
    Following context dictionary validations within the view process,
    posts the results to the database for reference and later retrieval.
    """
    NumbersGame.objects.create(
        game_nums=context['game_nums'],
        target_number=context['target_number'],
        player_num_achieved=context['player_num_achieved'],
        valid_calc=context['valid_calc'],
        comp_num_achieved=context['comp_num_achieved'],
        player_score=context['player_score'],
        comp_score=context['comp_score'],
        solution_str=context['solution_str'],
        game_result=context['game_result'],
    )
