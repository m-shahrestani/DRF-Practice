from rest_framework import serializers
from .models import Post, Rating
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['id']


class RatingSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(write_only=True)
    post_uuid = serializers.UUIDField(write_only=True)
    score = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rating
        fields = ['user_name', 'post_uuid', 'score', 'created_at', 'updated_at']

    def validate(self, data):
        try:
            data['user'] = User.objects.get(username=data.pop('user_name'))
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")
        try:
            data['post'] = Post.objects.get(uuid=data.pop('post_uuid'))
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post with this uuid does not exist.")
        return data
