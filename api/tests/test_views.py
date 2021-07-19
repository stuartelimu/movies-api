from django.http import response
from django.urls import reverse
from rest_framework.test import APITestCase

from api.models import Movie


class TestMovieAPI(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(name='The Space Between Us', year_of_release=2017)
    
    def test_movie_creation(self):
        response = self.client.post(reverse('movies'), {
            'name': 'Bee Movie',
            'year_of_release': 2007
        })

        # asert the movie was created 
        self.assertEqual(Movie.objects.count(), 2)

        # assert a created status code was created
        self.assertEqual(response.status_code, 201)

    def test_movie_list(self):
        response = self.client.get(reverse('movies'), format='json')
        self.assertEqual(len(response.data), 1)

    def test_update_movie(self):
        movie = Movie.objects.get(id=1)
        response = self.client.put(reverse('detail', kwargs={'pk':movie.id}), {
            'name': 'The Space Between Us Updated',
            'year_of_release': 2017
        }, format='json')

        movie.refresh_from_db()
    
        # check if movie was updated
        self.assertEqual(response.data['name'], 'The Space Between Us Updated')

    def test_delete_movie(self):
        response = self.client.delete(reverse('detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, 204)
