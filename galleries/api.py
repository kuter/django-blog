from rest_framework import viewsets

from .models import Gallery
from .serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
