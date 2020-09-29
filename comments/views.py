from .serializers import CommentsSerializer
from rest_framework import serializers
from .models import Comment
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
