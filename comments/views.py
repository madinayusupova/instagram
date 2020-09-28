from .serializers import CommentsSerializer
from rest_framework import serializers
from .models import Comment
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()


    def get(self, request):
        article = Comment.objects.all()
        serializer = serializers.CommentsSerializer(article, many=True)
        return Response({"article": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # print(type('type', article))
        serializer = serializers.CommentsSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "OK"})

    def delete(self, request, pk):
        article = get_object_or_404(Comment.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "ok"})