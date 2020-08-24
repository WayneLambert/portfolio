from apps.countdown_numbers.templatetags import template_helpers


def test_remove_brackets():
    test_value = '[100*9]'
    outcome = template_helpers.remove_brackets(test_value)
    assert '[' and ']' not in outcome, 'Square brackets should not be returned'

def test_add_spacing():
    test_value = '[(100*9)/(4+5)-1]'
    outcome = template_helpers.add_spacing(test_value)
    assert outcome == '[(100 * 9) / (4 + 5) - 1]'

def test_change_symbols():
    test_value = '(100 * 9) / (4 + 5) - 1'
    outcome = template_helpers.change_symbols(test_value)
    expected_outcome = '(100 ' + chr(215) +' 9) ' + chr(247) + ' (4 + 5) - 1'
    assert outcome == expected_outcome, \
        "Should be reformatted with mathematical multiplication and division symbols"

def test_humanise_calculation():
    test_value = '[(100*9)/(4+5)-1]'
    removed_brackets = template_helpers.remove_brackets(test_value)
    spacing_added = template_helpers.add_spacing(removed_brackets)
    overall_outcome = template_helpers.change_symbols(spacing_added)
    expected_outcome = '(100 ' + chr(215) +' 9) ' + chr(247) + ' (4 + 5) - 1'
    assert overall_outcome == expected_outcome, \
        """ Should have brackets removed, spacing added, and be
        reformatted with humanised mathematical multiplication and
        division symbols"""
