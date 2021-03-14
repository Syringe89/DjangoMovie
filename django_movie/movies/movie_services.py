from .models import Category, Genre, Movie


def get_title_from_params(**kwargs):
    if kwargs.get('category'):
        try:
            title = Category.objects.get(url=kwargs['category']).name
        except Category.DoesNotExist:
            title = 'Произведения'
    else:
        title = 'Произведения'

    if kwargs.get('genre'):
        try:
            title += f' жанра {Genre.objects.get(url=kwargs["genre"]).name}'
        except Genre.DoesNotExist:
            title += ' всех жанров'
    else:
        title += ' всех жанров'

    if kwargs.get('from') and kwargs.get('to'):
        if Movie.objects.filter(year=kwargs.get("from")).exists() and \
                Movie.objects.filter(year=kwargs.get("to")).exists():
            title += f' за {kwargs.get("from")} - {kwargs.get("to")} года'

    return title


def get_movie_from_params(**kwargs):
    queryset = Movie.objects.all()

    if kwargs.get('category', 'all') != 'all':
        queryset = queryset.filter(category__url=kwargs['category'])
    if kwargs.get('genre', 'all') != 'all':
        queryset = queryset.filter(genres__url=kwargs['genre'])
    if kwargs.get('from') and kwargs.get('to'):
        queryset = queryset.filter(year__range=(kwargs.get('from'), kwargs.get('to')))

    return queryset
