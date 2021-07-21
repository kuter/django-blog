from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('', views.PostListView.as_view(), name='list'),
]
