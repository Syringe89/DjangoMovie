from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
