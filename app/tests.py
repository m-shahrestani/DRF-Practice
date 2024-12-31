from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post, Rating

User = get_user_model()


class PostTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.post_url = '/posts/'

    def test_create_post(self):
        data = {
            "title": "Test Post",
            "content": "This is a test post content.",
        }
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post content.")


class RatingTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.post = Post.objects.create(title="Test Post", content="Test content")
        self.rating_url = '/ratings/'

    def test_create_rating(self):
        data = {
            "user_name": self.user.username,
            "post_uuid": str(self.post.uuid),
            "score": 5
        }
        response = self.client.post(self.rating_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Rating.objects.count(), 0)
