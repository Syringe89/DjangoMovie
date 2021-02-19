from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies.models import Movie


class MovieView(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movie_list'


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    slug_url_kwarg = 'url'
    template_name = 'movies/movie_detail.html'
    # template_name = 'movies/test.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['actors'] = Movie.objects.get(url=self.kwargs['url']).actors.all()
        return context

