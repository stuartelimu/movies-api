from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'name', 'year_of_release')
        read_only_fields = ('id',)