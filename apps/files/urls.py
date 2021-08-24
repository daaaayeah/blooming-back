from django.urls import path

from .views import FileListCreateAPIView


urlpatterns = [
    path('files/', FileListCreateAPIView.as_view())
]
