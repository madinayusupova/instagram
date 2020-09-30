from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from post.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer
from post.models import Post
from post.permissions import IsOwnerorReadOnly
from rest_framework import permissions, filters

class MyPaginationClass(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 255



class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated, )



class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    search_fields = ['author__username', 'text']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()

    # queryset = Post.objects.filter(author.id = user.following.id)
    # permission_classes = (permissions.IsAuthenticated, )
    pagination_class = MyPaginationClass

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerorReadOnly, )
#
# class PostSearchListView(generics.ListAPIView):
#     search_fields = ['author']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = PostListSerializer
#     queryset = Post.objects.all()
#     # permission_classes = (permissions.IsAuthenticated,)
#     pagination_class = MyPaginationClass
#

