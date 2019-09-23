from django import forms
from django.core.validators import RegexValidator, ValidationError


class NumberSelectionForm(forms.Form):
    num_from_top = forms.IntegerField(
        label='',
        required=True,
        min_value=0,
        max_value=4,
    )


class SelectedNumbersForm(forms.Form):
    permissible_chars = RegexValidator(
        r'^[0-9()\+\-\*\/]*$', 'Only arithmetic symbols, numbers, and rounded brackets permitted.')

    def brackets_validation(players_calc): # pylint: disable=no-self-argument
        if players_calc.count('(') != players_calc.count(')'):
            raise ValidationError(
                'Please ensure the number of opening and closing brackets match.',
                params={'players_calc': players_calc},
            )

    def spaces_check(players_calc): # pylint: disable=no-self-argument
        if ' ' in players_calc:
            raise ValidationError(
                'Please ensure there are no spaces within your calculation.'
            )

    players_calculation = forms.CharField(
        label="Enter the calculation for the closest number you can arrive at here...",
        required=True,
        strip=True,
        min_length=3,
        max_length=29,
        validators=[permissible_chars, spaces_check, brackets_validation],
    )
