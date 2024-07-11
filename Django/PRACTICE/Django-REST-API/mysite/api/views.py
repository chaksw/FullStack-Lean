from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # override http method delete() defined in http_method_names of class view in django
    # def delete(self, request, *args, **kwargs):
    #     BlogPost.objects.all().delete()  # delete all objects
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # primary key


class BlogPostList(APIView):
    # override http method get()
    def get(self, request, format=None):
        # Get the title from the query parameters (if none, default to empty string)
        # 获取 ‘title’ 查询参数的值
        title = request.query_params.get("title", "")

        if title:
            # Filter the queryset based on the title
            # title_icontains used to perform a case-insensitive search
            blog_post = BlogPost.objects.filter(title_icontains=title)
        else:
            # If no title is provided, return all blog posts
            blog_post = BlogPost.objects.all()

        # create an Serializer instance, many=True tells the serializer that it should expect multiple instance of the object type and serialize each one individually.
        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
