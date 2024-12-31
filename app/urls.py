from django.urls import path
from .views import PostViewSet, RatingViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('rating/', RatingViewSet.as_view({'put': 'update', 'post': 'create'}), name='rating-update'),
]

urlpatterns += router.urls
