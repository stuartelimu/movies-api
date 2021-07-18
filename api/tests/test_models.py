from django.test import TestCase

from api.models import Movie


class TestMovieModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(name="Split", year_of_release=2016)

    def test_movie_creation(self):
        self.assertEqual(Movie.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEqual(self.movie.name, str(self.movie))

