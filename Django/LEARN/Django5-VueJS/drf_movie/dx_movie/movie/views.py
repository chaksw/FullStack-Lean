from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from .models import Movie
# from .serializers import MovieListSerializer, MoviewDetailSerializer
from .serializers import MovieSerializer
# Create your views here.

'''
def movie_list(request):
    # 获取数据
    if request.method == 'GET':
        # values_list 将数据转化为列表
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        # data = list(movies)
        # data = {
        #     'movie_name': '碟中谍',
        #     'rate': 7.8
        # }
        return JsonResponse(serializer.data, safe=False)
'''

# 基于 Django rest framework api_view 的 视图功能
'''
@api_view(['GET', 'POST'])
def movie_list(request):
    # 获取数据
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        # ModelSerializer 提供了与 Django 数据模型对应的操作方法，我们在对 serializer 对象进行操作的同时也将同时对model进行操作，这里 is_valid() save()的方法就是操作 serializer 对象的同时对绑定的模型进行操作
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


# 基于 Django rest framework APIVIEW (CBV) 实现列表详情页(CURD)功能
'''
class MovieDetail(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404
        serializer = MoviewDetailSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404
        serializer = MovieListSerializer(movie, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


# ======================================================================
# 基于 django rest framework ListCreateAPIView 实现视图列表展示和新增功能
'''
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
'''


# ======================================================================
# 基于 Django rest framework GenericAPIView （通用视图）,以及 Mixin 类实现列表详情页(CURD)功能
# GenericAPIView 是 APIVIEW 的子类，它基于 APIVIEW 提供了额外的便捷功能如： 定义 query_set, serializer_class
# mixins.RetrieveModelMixin: 获取数据相关的类
# mixins.UpdateModelMixin： 更新数据相关的类
# mixins.DestroyModelMixin： 删除数据相关的类
# 上述的类为我们实现了常规的CURD功能，只需要定义好 queryset & serializer_class, 就能直接功能
# class MovieDetail(mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericAPIView):
# django rest framework 中还拥有融合了多个GenericAPIView, Mixin 类的子类
# CreateAPIView(RetrieveModelMixin, GenericAPIView)
# UpdateAPIView(UpdateModelMixin, GenericAPIView)
# DestroyAPIView(DestroyAPIView, GenericAPIView)
# RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
#    mixins.UpdateModelMixin,
#    mixins.DestroyModelMixin,
#    GenericAPIView):
'''
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviewDetailSerializer
'''
# RetrieveUpdateDestroyAPIView 中已经实现了如下功能，我们只需要定义好queryset & serializer_class即可
# 注意更新数据不再使用put()调用 partial_update()，而是使用 patch()
# def get(self, request, *args, **kwargs):
#     # 获取数据
#     return self.retrieve(request=request, *args, **kwargs)

# def put(self, reqeust, *args, **kwargs):
#     # 更新数据
#     # 使用 UpdateModelMixin 中的 partial_update()
#     return self.partial_update(request=reqeust, *args, **kwargs)

# def delete(self, request, *args, **kwargs):
#     # 删除数据
#     return self.destroy(request=request, *args, **kwargs)


# ======================================================================
# 基于 django rest framework 的视图集 viewsets.ModelViewSet ，将针对一个数据模型的列表/新增/查看/更新/删除功能结合在一个 serializerclass 中
# ModelViewSet 融合了 GenericAPIView 中对一个数据模型的所有 http 操作相关的类
# class ModelViewSet(mixins.CreateModelMixin,
#    mixins.RetrieveModelMixin,
#    mixins.UpdateModelMixin,
#    mixins.DestroyModelMixin,
#    mixins.ListModelMixin,
#    GenericViewSet):
# 从实现来看，本质上是将对某一个资源（url) 的所有 http 操作打包成一个 api 接口
# benefit：
# 1. 在 serializers.py 中，不再需要分开 MovieListSerializer, MoviewDetailSerializer
# 2. 在路由 urls.py 中，不需要分别为视图列表和单个数据视图操作定路由，而只需要采取注册的方式即可
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
