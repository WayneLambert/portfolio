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
