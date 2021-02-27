from django.urls import path

from movies.views import *

urlpatterns = [
    path('', MovieView.as_view(), name='home'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/<slug:slug>/add_review/', MovieAddReviewView.as_view(), name='add_review'),
]
