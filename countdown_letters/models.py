from django.db import models


class LettersGame(models.Model):
    letters_chosen = models.CharField(max_length=9)
    players_word = models.CharField(max_length=9)
    comp_word = models.CharField(max_length=9)
    eligible_answer = models.BooleanField(default=False)
    winning_word = models.CharField(max_length=9)
    player_word_len = models.IntegerField(default=0)
    comp_word_len = models.IntegerField(default=0)
    player_score = models.IntegerField(default=0)
    comp_score = models.IntegerField(default=0)
    definition = models.TextField()
    word_class = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    entry_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-entry_date', )

    @property
    def entry_year(self) -> int:
        return self.entry_date.year
