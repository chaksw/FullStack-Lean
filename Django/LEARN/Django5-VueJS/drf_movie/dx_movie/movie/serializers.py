from rest_framework import serializers

from .models import Movie

# class MovieListSerializer(serializers.Serializer):


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ['movie_name', 'release_year', 'director', 'actors']
