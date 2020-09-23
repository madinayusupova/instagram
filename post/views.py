from django.shortcuts import render
from rest_framework import generics
from post.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer
from post.models import Post


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()



