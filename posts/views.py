from django.views.generic import DetailView, ListView

from .models import Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    queryset = Post.objects.all()
