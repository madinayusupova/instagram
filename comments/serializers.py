from rest_framework import serializers
from . import models

class CommentsSerializer(serializers.Serializer):
    body = serializers.CharField(required=False, allow_blank=True, max_length=300)
    id_ = serializers.IntegerField(read_only=True)

    
    def create(self, validated_data):
        return models.Comment.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    class Meta:
        model = models.Comment
        fields = ('id', 'post', 'body', 'author')