from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ['id', 'name', 'url']
    list_display_links = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


class ReviewsInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']
    raw_id_fields = ['parent']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'url': ('title',)}
    list_display = ['id', 'title', 'category', 'url', 'draft']
    list_display_links = ['title']
    list_filter = ['category', 'year']
    search_fields = ['title', 'category__name']
    list_editable = ['draft']
    fieldsets = [
        (None, {
            'fields': (('title', 'tagline'),)
        })
    ]
    save_on_top = True
    save_as = True
    inlines = [ReviewsInLine]


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'parent', 'movie']
    list_filter = ['name', 'movie']
    readonly_fields = ['name', 'email']


admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
