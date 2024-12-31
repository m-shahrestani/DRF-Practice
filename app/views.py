from rest_framework import viewsets
from .models import Rating, Post
from .serializers import PostSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from django.utils import timezone


class PostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Post.objects.order_by('title').all()
    serializer_class = PostSerializer


class RatingViewSet(viewsets.ViewSet):
    http_method_names = ['post', 'put']

    def update_post_avarage(self, post, score, old_score=None):
        if post.ratings_count > 10 and timezone.now() - post.updated_at < timedelta(seconds=10):
            score *= 0.01
        if old_score is not None:
            post.average_score = ((post.average_score * post.ratings_count) - old_score + score) / post.ratings_count
        else:
            post.average_score = ((post.average_score * post.ratings_count) + score) / (post.ratings_count + 1)
            post.ratings_count += 1
        post.save()

    def create(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            post = serializer.validated_data['post']
            score = serializer.validated_data['score']
            if Rating.objects.filter(user=user, post=post).exists():
                return Response({"error": "Rating already exists."}, status=status.HTTP_400_BAD_REQUEST)
            rating = Rating.objects.create(user=user, post=post, score=score)
            self.update_post_avarage(post, score)
            return Response(
                {"message": "Rating created successfully.", "score": rating.score},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            post = serializer.validated_data['post']
            score = serializer.validated_data['score']
            try:
                rating = Rating.objects.get(user=user, post=post)
            except Rating.DoesNotExist:
                return Response({"error": "Rating does not exist."}, status=status.HTTP_404_NOT_FOUND)
            old_score = rating.score
            rating.score = score
            rating.save()
            self.update_post_avarage(post, score, old_score)
            return Response(
                {"message": "Rating updated successfully.", "score": rating.score},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
