from django.contrib import admin
from django.db import models
from django.forms.widgets import Textarea, TextInput

from apps.countdown_letters.models import LettersGame


class LettersGameAdmin(admin.ModelAdmin):
    model = LettersGame
    list_display = (
        'letters_chosen', 'players_word', 'comp_word', 'winning_word', 'entry_date')
    ordering = ('-entry_date',)
    readonly_fields = [field.name for field in LettersGame._meta.get_fields()]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 60})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '2'})},
    }

    fieldsets = (
        ('Selection', {
            'fields': ['letters_chosen']
        }),
        ('Game', {
            'fields': (('players_word', 'eligible_answer', 'comp_word', 'winning_word'))
        }),
        ('Results', {
            'fields': (
                ('player_word_len', 'player_score'),
                ('comp_word_len', 'comp_score')
            )
        }),
        ('Definition', {
            'fields': ('word_class', 'definition',)
        }),
        ('Dates', {
            'fields': ('entry_date', )
        }),
    )


admin.site.register(LettersGame, LettersGameAdmin)
