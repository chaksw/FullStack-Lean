from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost  # define model to map
        fields = ["id", "title", "content", "published_date"]
