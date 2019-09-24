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
        required=True,
        label='',
        help_text="""Valid calc example: (((25+75)*4)/4)+1 |
        Invalid calc example: (((25+75* 4)/ 4)+1z""",
        max_length=29,
        min_length=3,
        strip=True,
    )
