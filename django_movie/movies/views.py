from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from movies.forms import MovieAddReviewForm
from movies.models import Movie, Rating, Category, Genre


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
        context['form'] = MovieAddReviewForm()
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
        if self.kwargs.get('category'):
            context['title'] = Category.objects.get(url=self.kwargs['category']).name
        else:
            context['title'] = 'Произведения'
        if self.kwargs.get('genre'):
            context['title'] += f' жанра {Genre.objects.get(url=self.kwargs["genre"]).name}'
        else:
            context['title'] += ' всех жанров'
        return context

    def get_queryset(self):
        queryset = Movie.objects.all()

        if self.kwargs.get('category'):
            queryset = queryset.filter(category__url=self.kwargs['category'])
        if self.kwargs.get('genre'):
            queryset = Movie.objects.filter(genres__url=self.kwargs['genre'])
        return queryset


class MovieListFilterView(ListView):
    template_name = 'movies/movie_list_grid.html'
    context_object_name = 'movie_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieListFilterView, self).get_context_data(object_list=None, **kwargs)
        if self.request.GET.get('category') != 'all':
            context['title'] = Category.objects.get(url=self.request.GET.get('category')).name
        else:
            context['title'] = 'Произведения'
        if self.request.GET.get('genre') != 'all':
            context['title'] += f' жанра {Genre.objects.get(url=self.request.GET.get("genre")).name}'
        else:
            context['title'] += ' всех жанров'
        context['title'] += f' за {self.request.GET.get("from")} - {self.request.GET.get("to")}'
        return context

    def get_queryset(self):
        queryset = Movie.objects.all()
        if self.request.GET.get('category') != 'all':
            queryset = queryset.filter(category__url=self.request.GET.get('category'))
        if self.request.GET.get('genre') != 'all':
            queryset = queryset.filter(genres__url=self.request.GET.get('genre'))
        queryset = queryset.filter(year__range=(self.request.GET.get('from'), self.request.GET.get('to')))

        return queryset
