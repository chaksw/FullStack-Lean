from django.shortcuts import render
from django.http import JsonResponse

from .models import Movie
from .serializers import MovieListSerializer
# Create your views here.


def movie_list(request):
    # 获取数据
    # values_list 将数据转化为列表
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    # data = list(movies)
    # data = {
    #     'movie_name': '碟中谍',
    #     'rate': 7.8
    # }
    return JsonResponse(serializer.data, safe=False)
