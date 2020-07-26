from django.db import models


class NumbersGame(models.Model):
    game_nums = models.CharField(max_length=255)
    target_number = models.IntegerField()
    player_num_achieved = models.IntegerField()
    valid_calc = models.BooleanField(default=False)
    comp_num_achieved = models.IntegerField()
    player_score = models.IntegerField(default=0)
    comp_score = models.IntegerField(default=0)
    solution_str = models.CharField(max_length=255)
    game_result = models.CharField(max_length=255)
    entry_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-entry_date', )

    @property
    def entry_year(self) -> int:
        return self.entry_date.year

    @staticmethod
    def create_record(context: dict):
        """
        Following context dictionary validations within the view
        process, posts the results to the database for reference and
        later retrieval.
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
