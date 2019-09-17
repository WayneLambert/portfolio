from django import forms
from django.core.validators import RegexValidator


class NumberSelectionForm(forms.Form):
    num_from_top = forms.IntegerField(
        label='',
        required=True,
        min_value=0,
        max_value=4,
    )


class SelectedNumbersForm(forms.Form):
    permissible_chars = RegexValidator(
        r'^[0-9()\+\-\*\/]*$', 'Only calculation characters are allowed.')

    players_calculation = forms.CharField(
        label="Enter the calculation for the closest number you can arrive at here...",
        required=True,
        strip=True,
        validators=[permissible_chars]
    )
