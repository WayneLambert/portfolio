from django import forms


class LetterSelectionForm(forms.Form):
    num_vowels_selected = forms.IntegerField(
        required=True, label='', min_value=3, max_value=5)


class SelectedLettersForm(forms.Form):
    players_word = forms.CharField(
        required=True,
        label='',
        strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your word...'})
    )
