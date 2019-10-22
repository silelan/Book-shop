from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
@stringfilter

def multiply(qty, price, *args, **kwargs):
    # you would need to do any localization of the result here
    return float(qty) * float(price)