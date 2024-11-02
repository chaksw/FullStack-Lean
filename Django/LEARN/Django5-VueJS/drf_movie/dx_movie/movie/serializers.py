from rest_framework import serializers

from .models import Movie, Category

# class MovieListSerializer(serializers.Serializer):


# ModelSerializer 提供了与 Django 数据模型的数据类型的映射，所以可以直接通过创建meta类绑定对应的model来实现serializer model 的建立
# class MovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'


# class MoviewDetailSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie
#         fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
