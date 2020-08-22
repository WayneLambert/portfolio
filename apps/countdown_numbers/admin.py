from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput

from apps.countdown_numbers.models import NumbersGame


class NumbersGameAdmin(admin.ModelAdmin):
    model = NumbersGame
    list_display = (
        'game_nums', 'target_number', 'player_num_achieved',
        'comp_num_achieved', 'game_result', 'entry_date'
    )
    ordering = ('-entry_date',)
    readonly_fields = [field.name for field in NumbersGame._meta.get_fields()]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.IntegerField: {'widget': TextInput(attrs={'size': '2'})},
    }

    fieldsets = (
        ('Selection', {
            'fields': ['game_nums', 'target_number']
        }),
        ('Results', {
            'fields': (
                ('valid_calc', 'player_num_achieved', 'player_score'),
                ('comp_num_achieved', 'comp_score'),
                'solution_str',
                'game_result'
            )
        }),
        ('Dates', {
            'fields': ('entry_date', )
        }),
    )

admin.site.register(NumbersGame, NumbersGameAdmin)
