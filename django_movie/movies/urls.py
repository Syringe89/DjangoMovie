from django.urls import path

from movies.views import *

urlpatterns = [
    path('', MovieView.as_view()),
    path('movie/<slug:url>/', MovieDetailView.as_view(), name='movie_detail'),
]
