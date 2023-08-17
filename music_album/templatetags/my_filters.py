from django import template

register = template.Library()

def my_filter(value):
    return value + "This is value from custom filter"

register.filter('custom_filter', my_filter)