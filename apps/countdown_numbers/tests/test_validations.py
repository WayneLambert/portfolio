import pytest

from apps.countdown_numbers import validations


@pytest.mark.django_db
class TestCheckChars:
    def test_valid_calc_string(self):
        """Checks a calc without illegal characters passes"""
        calc = "(((25+75)*4)/4)+1"
        check_passes = validations.check_chars(calc)
        assert check_passes, "Should return `True`"

    def test_invalid_calc_string(self):
        """Checks a calc with illegal characters doesn't pass"""
        calc = "(((25+75)*4)^4)+1"  # Includes caret symbol
        check_passes = validations.check_chars(calc)
        assert not check_passes, "Should return `False`"


class TestCheckBrackets:
    def test_valid_calc_string(self):
        """Checks a calc with a valid bracket pairing passes"""
        calc = "(((25+75)*4)/4)+1"
        check_passes = validations.check_brackets(calc)
        assert check_passes, "Should return `True`"

    def test_invalid_calc_string(self):
        """Checks a calc with an invalid bracket pairing doesn't pass"""
        calc = "(((25+75)*4)/4))+1"  # 3 opening; 4 closing brackets
        check_passes = validations.check_brackets(calc)
        assert not check_passes, "Should return `False`"


class TestCheckLegalChars:
    def test_valid_calc_string(self):
        """Checks a calc with a valid characters passes"""
        calc = "(((25+75)*4)/4)+1"
        check_passes = validations.check_legal_chars_seq(calc)
        assert check_passes, "Should return `True`"

    def test_invalid_calc_string(self):
        """Checks a calc with invalid characters doesn't pass"""
        calc = "(((25+75)*4)/4)+1/)"  # Includes '/)'
        check_passes = validations.check_legal_chars_seq(calc)
        assert not check_passes, "Should return `False`"


class TestStripSpaces:
    def test_stripped(self):
        """Checks spaces are stripped from calc"""
        calc = " (((25 + 75) * 4 )/ 4 ) + 1 "  # Includes spaces
        stripped = validations.strip_spaces(calc)
        assert " " not in stripped
        assert stripped == "(((25+75)*4)/4)+1"


class TestValidCalc:
    def test_valid_calc_passes_checks(self):
        """Checks that a valid calc string passes the checks"""
        players_calc = "50 * 10"
        checks = validations.calc_entered_is_valid(players_calc)
        assert checks.has_valid_brackets
        assert checks.has_valid_chars
        assert checks.has_valid_sequences

    def test_invalid_brackets_fails_check(self):
        """Asserts a calc string with invalid brackets fails the checks"""
        players_calc = "(50 * 10))"
        checks = validations.calc_entered_is_valid(players_calc)
        assert isinstance(checks, tuple)
        assert not checks.has_valid_brackets

    def test_invalid_chars_fails_check(self):
        """Asserts a calc string with invalid chars fails the checks"""
        players_calc = "50 * 10z"
        checks = validations.calc_entered_is_valid(players_calc)
        assert isinstance(checks, tuple)
        assert not checks.has_valid_chars

    def test_invalid_sequences_fails_check(self):
        """Asserts a calc string with invalid sequences fails the checks"""
        players_calc = "(50 * 10/)"
        checks = validations.calc_entered_is_valid(players_calc)
        assert isinstance(checks, tuple)
        assert not checks.has_valid_sequences
