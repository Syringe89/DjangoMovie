from django.utils.safestring import mark_safe
from .models import *


class GetImageMixin:
    image_width = '60'
    image_height = 'auto'

    def get_image(self, obj):
        if hasattr(obj, 'image') and obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width={self.image_width} height="{self.image_height}">')
        elif hasattr(obj, 'poster') and obj.poster:
            return mark_safe(
                f'<img src="{obj.poster.url}" width={self.image_width} height="{self.image_height}">')
        else:
            return 'Фото не установлено'

    get_image.short_description = 'Миниатюра'


class MovieFilterMixin:

    def get_categories(self):
        return Category.objects.all()
