from django import forms


class NumberSelectionForm(forms.Form):
    num_from_top = forms.IntegerField(required=True, label='', min_value=0, max_value=4)


class SelectedNumbersForm(forms.Form):
    players_calculation = forms.CharField(
        required=True,
        label='',
        strip=True,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your calculation closest to the target number...'}),
    )
