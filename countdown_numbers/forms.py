from django import forms


class NumberSelectionForm(forms.Form):
    num_from_top = forms.IntegerField(
        label='',
        required=True,
        min_value=0,
        max_value=4,
    )


class SelectedNumbersForm(forms.Form):
    players_calculation = forms.CharField(
        label="Enter the calculation for the closest number you can arrive at here...",
        required=True,
        strip=True,
    )
