from django import template

register = template.Library()

@register.filter(name='cutter')
def cut(value, arg):
    """
    this cuts out from the string

    """
    return value.replace(arg,'')
