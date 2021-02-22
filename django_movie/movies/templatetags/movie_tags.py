from django import template
from django.core.exceptions import FieldDoesNotExist

register = template.Library()


@register.simple_tag()
def get_verbose_name(self, field_name):
    """
    Шаблонный тег, возвращающий verbose_name поля field_name из модели
    """

    try:
        value = self._meta.get_field(field_name).verbose_name
    except (AttributeError, FieldDoesNotExist):
        return field_name
    return value
