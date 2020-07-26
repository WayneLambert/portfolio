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

    @staticmethod
    def create_record(context: dict):
        """
        Following context dictionary validations within the view
        process, posts the results to the database for reference and
        later retrieval.
        """
        LettersGame.objects.create(
            letters_chosen=context['letters_chosen'],
            players_word=context['players_word'],
            comp_word=context['comp_word'],
            eligible_answer=context['eligible_answer'],
            winning_word=context['winning_word'],
            player_word_len=context['player_word_len'],
            comp_word_len=context['comp_word_len'],
            player_score=context['player_score'],
            comp_score=context['comp_score'],
            definition=context['definition_data']['definition'],
            word_class=context['definition_data']['word_class'],
            result=context['result'],
        )
