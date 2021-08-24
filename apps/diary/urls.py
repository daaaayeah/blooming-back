from django.urls import path

from .views import DiaryListCreateAPIView, DiaryRetrieveUpdateDestroyAPIView, DiaryLikeAPIView, DiaryUnlikeAPIView


urlpatterns = [
    path('diary/', DiaryListCreateAPIView.as_view()),
    path('diary/<diary_pk>', DiaryRetrieveUpdateDestroyAPIView.as_view()),
    path('diary/<diary_pk>/like', DiaryLikeAPIView.as_view()),
    path('diary/<diary_pk>/unlike', DiaryUnlikeAPIView.as_view())
]
