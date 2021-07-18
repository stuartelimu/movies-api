from django.urls import path

from .views import MovieCreateView, MovieDetailView

urlpatterns = [
    path('movies/', MovieCreateView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='detail'),
]
