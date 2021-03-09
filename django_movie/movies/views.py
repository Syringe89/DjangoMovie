from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from movies.forms import MovieAddReviewForm
from movies.models import Movie, Rating
from .utils import MovieFilterMixin


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

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['form'] = MovieAddReviewForm()
        return context

    def get_queryset(self):
        return super().get_queryset().prefetch_related('actors', 'directors', 'movieshots_set')


class MovieAddReviewView(View):
    def post(self, request, slug):
        form = MovieAddReviewForm(request.POST)
        movie = Movie.objects.get(url=slug)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie)
