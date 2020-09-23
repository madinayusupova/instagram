from rest_framework import serializers
from post.models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'author', 'text')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('text')
