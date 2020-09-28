from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import CommentAPIView

router = SimpleRouter()
router.register("", CommentAPIView)


urlpatterns = [
    path('', include(router.urls)),
]
