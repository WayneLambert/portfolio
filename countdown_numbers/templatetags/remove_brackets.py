from django import template

register = template.Library()


@register.filter
def remove_brackets(value):
    return value.replace("[", "").replace("]", "")
