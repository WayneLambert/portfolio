from django import template

register = template.Library()


@register.filter
def remove_brackets(value):
    return value.replace("[", "").replace("]", "")

@register.filter
def change_symbols(value):
    return value.replace("*", chr(10005)).replace("/", u"\u00F7")
