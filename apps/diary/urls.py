from django.urls import path

from .views import DiaryListCreateAPIView, DiaryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('diary/', DiaryListCreateAPIView.as_view()),
    path('diary/', DiaryRetrieveUpdateDestroyAPIView.as_view())
]
