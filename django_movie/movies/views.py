from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import *
from movies.models import Movie, Rating, Category, Genre
from movies.movie_services import *


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
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['add_review_form'] = MovieAddReviewForm()
        context['add_rating_form'] = MovieAddRatingForm()
        return context

    def get_queryset(self):
        return super().get_queryset().prefetch_related('actors', 'directors', 'movieshots_set')


class MovieAddReviewView(View):
    def post(self, request, **kwargs):
        form = MovieAddReviewForm(request.POST)
        movie = Movie.objects.get(url=kwargs['slug'])
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie)


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list_grid.html'
    context_object_name = 'movie_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = get_title_from_params(**self.kwargs)
        return context

    def get_queryset(self):
        return get_movie_from_params(**self.kwargs)


def filtered_movies_redirect(request):
    return redirect('movie_list', request.GET.get('category'), request.GET.get('genre'),
                    request.GET.get('from'), request.GET.get('to'))

