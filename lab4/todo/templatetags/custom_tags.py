from django import template
import random

register = template.Library()

@register.simple_tag
def my_custom_tag():
    # return "Hello custom tag"
    return random.randint(1, 100)

@register.filter
def my_filter(data):
    return data[:50]