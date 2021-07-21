from django.urls import path

from . import views

app_name = 'galleries'

urlpatterns = [
    path('', views.GalleryListView.as_view(), name='list'),
]
