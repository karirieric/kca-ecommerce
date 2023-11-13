from django import template

register = template.Library()

@register.filter
def format_price(value):
    return '{:,.0f}'.format(value)
