from django.urls import path

from movies.views import *

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('movie/filter/', MovieListFilterView.as_view(), name='movie_list_filter'),
    path('movie/<category>/', MovieListView.as_view(), name='movie_list'),
    path('movie/<category>/<genre>/', MovieListView.as_view(), name='movie_list'),
    path('movie/<category>/<genre>/<from>/', MovieListView.as_view(), name='movie_list'),
    path('movie/<category>/<genre>/<from>-<to>/', MovieListView.as_view(), name='movie_list'),
    path('movie/<category>/<genre>/<slug>', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/<category>/<genre>/<slug>/add_review/', MovieAddReviewView.as_view(), name='add_review'),
]
