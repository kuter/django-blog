from django.views.generic import ListView

from .models import Gallery


class GalleryListView(ListView):
    queryset = Gallery.objects.all()
