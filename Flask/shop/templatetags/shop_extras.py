from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Template filter to get item from dictionary by key.
    Usage: {{ dict|get_item:key }}
    """
    if dictionary and hasattr(dictionary, 'get'):
        return dictionary.get(key)
    return None

@register.filter
def get_attr(obj, attr_name):
    """
    Template filter to get attribute from object.
    Usage: {{ obj|get_attr:attr_name }}
    """
    try:
        return getattr(obj, attr_name, None)
    except (AttributeError, TypeError):
        return None