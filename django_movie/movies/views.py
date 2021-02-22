from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies.models import Movie, Rating


class MovieView(ListView):
    model = Movie
    template_name = 'movies/movie_index.html'
    # template_name = 'movies/test.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_detail.html'
    # template_name = 'movies/test.html'
    context_object_name = 'movie'
    queryset = Movie.objects.prefetch_related('actors', 'directors')

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        return context
