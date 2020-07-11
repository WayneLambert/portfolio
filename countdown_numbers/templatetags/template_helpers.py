""" Template Helpers

Functions to assist in the presentation of the game's calculations
to humanise the game to be in a presentable arithmetic format
"""

from django import template

register = template.Library()


@register.filter
def remove_brackets(value):
    """ Removes any squared brackets """
    return value.replace("[", "").replace("]", "")

@register.filter
def add_spacing(value):
    """ Adds spacing around the calculation's operators """
    s = value.replace("+", " + ")
    s = s.replace("-", " - ")
    s = s.replace("*", " * ")
    s = s.replace("/", " / ")
    return s

@register.filter
def change_symbols(value):
    """
    Changes asterisks and backslashes into arithmetic
    multiplication and division symbols.
    """
    return value.replace("*", chr(215)).replace("/", chr(247))
