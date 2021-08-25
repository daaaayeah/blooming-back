from django.urls import path

from .views import (
    DiaryListCreateAPIView,
    DiaryRetrieveUpdateDestroyAPIView,
    DiaryLikeAPIView,
    DiaryUnlikeAPIView,
    DiaryListRandomAPIView,
    DiarySentimentScoreAPIView,
    DiaryCountAPIView,
    DiarySharedAPIView,
    DiaryStatsAPIView,
    DiaryLikedAPIView
)


urlpatterns = [
    path('diary/', DiaryListCreateAPIView.as_view()),
    path('diary/<diary_pk>', DiaryRetrieveUpdateDestroyAPIView.as_view()),
    path('diary/<diary_pk>/like', DiaryLikeAPIView.as_view()),
    path('diary/<diary_pk>/unlike', DiaryUnlikeAPIView.as_view()),
    path('diary/random/', DiaryListRandomAPIView.as_view()),
    path('diary/score/', DiarySentimentScoreAPIView.as_view()),
    path('diary/count/', DiaryCountAPIView.as_view()),
    path('diary/shared/', DiarySharedAPIView.as_view()),
    path('diary/stats/', DiaryStatsAPIView.as_view()),
    path('diary/liked/', DiaryLikedAPIView.as_view())
]
