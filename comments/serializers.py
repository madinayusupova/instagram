from rest_framework import serializers
from . import models

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields =('id',)