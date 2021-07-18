from django.db.models import query
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# , MovieDetailView
from .models import Movie
from .serializers import MovieSerializer

class MovieCreateView(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

