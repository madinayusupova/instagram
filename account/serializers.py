from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserFollowing

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email',   "following", "followers",)
        extra_kwargs = {"password": {"write_only": True}}

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowersSerializer(obj.followers.all(), many=True).data

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "following_user_id", "created")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")
