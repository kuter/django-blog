from rest_framework import routers

from posts.api import PostViewSet
from galleries.api import GalleryViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'galleries', GalleryViewSet)
