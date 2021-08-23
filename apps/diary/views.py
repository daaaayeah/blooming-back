from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Diary
from .serializers import DiarySerializer


class DiaryListCreateAPIView(ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]


class DiaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    lookup_url_kwarg = 'diary_pk'
