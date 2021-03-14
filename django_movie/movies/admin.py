from django import forms
from django.contrib import admin
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from .models import *
from .utils import GetImageMixin

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}
    list_display = ['id', 'name', 'url']
    list_display_links = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']
    raw_id_fields = ['parent']

    def get_queryset(self, request):
        queryset = super(ReviewsInline, self).get_queryset(request).prefetch_related('movie')
        return queryset


class MovieShotsInline(admin.TabularInline, GetImageMixin):
    image_width = 100
    model = MovieShots
    extra = 1
    readonly_fields = ['get_image']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin, GetImageMixin):
    image_width = '100'
    prepopulated_fields = {'url': ('title',)}
    list_display = ['id', 'title', 'category', 'url', 'draft', 'year']
    list_display_links = ['title']
    list_filter = ['category', 'year']
    search_fields = ['title', 'category__name']
    list_editable = ['draft', 'year']
    readonly_fields = ['get_image']
    form = MovieAdminForm
    fieldsets = [
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'),)
        }),
        (None, {
            'fields': (('year', 'country'),)
        }),
        (None, {
            'fields': (('directors', 'actors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('world_premiere', 'budget', 'fees_in_usa', 'fess_in_world'),)
        }),
        (None, {
            'fields': (('url', 'draft'),)
        }),
    ]
    save_on_top = True
    save_as = True
    # inlines = [MovieShotsInline, ReviewsInline]
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        draft_updated = queryset.update(draft=False)

        self.message_user(request, f'{draft_updated} '
                                   f'{"запись была обновлена" if draft_updated == 1 else "записей было обновлено"}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    def unpublish(self, request, queryset):
        draft_updated = queryset.update(draft=True)

        self.message_user(request, f'{draft_updated} '
                                   f'{"запись была обновлена" if draft_updated == 1 else "записей было обновлено"}')

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'parent', 'movie']
    list_filter = ['name', 'movie']
    readonly_fields = ['name', 'email']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin, GetImageMixin):
    list_display = ['name', 'get_image']
    list_display_links = ['name', 'get_image']
    readonly_fields = ['get_image']


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin, GetImageMixin):
    list_display = ['title', 'get_image', 'movie']
    list_display_links = ['title', 'get_image']
    list_filter = ['movie']
    readonly_fields = ['get_image']


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['value']


admin.site.register(Rating)
admin.site.site_title = 'Администрирование'
admin.site.site_header = 'Администрирование'
