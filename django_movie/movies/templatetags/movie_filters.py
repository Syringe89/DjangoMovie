import re

from django import template

register = template.Library()


@register.filter()
def thousands_separator(value):
    """
    Шаблонный фильтр для поразрядного вывода чисел
    1234567890 -> 1 234 567 890
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    return f"{value:,}".replace(',', ' ')
