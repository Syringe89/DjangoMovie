from django import template
from django.core.exceptions import FieldDoesNotExist
from ..models import Category, Genre, Movie

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


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.simple_tag()
def get_years():
    return Movie.objects.all().order_by('year').values_list('year', flat=True).distinct()
