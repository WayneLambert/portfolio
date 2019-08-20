from django import forms

class LetterSelectionForm(forms.Form):
    num_vowels_selected = forms.IntegerField(
        label='',
        required=True,
        min_value=3,
        max_value=5,
    )


class SelectedLettersForm(forms.Form):
    players_word = forms.CharField(
        label="Enter the longest word you can find here...",
        required=True,
        strip=True,
    )
