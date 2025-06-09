from django import template
from urllib.parse import urlencode

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Custom filter to access dictionary values safely.
    """
    return dictionary.get(key)

@register.simple_tag
def query_string(**kwargs):
    """
    Custom tag to generate URL-encoded query string, preserving existing parameters.
    """
    query_params = {key: value for key, value in kwargs.items() if value is not None}
    return urlencode(query_params)