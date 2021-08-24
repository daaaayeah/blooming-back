from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import Diary
from .serializers import DiarySerializer
from apps.files.models import File
from apps.utils.language import sample_analyze_sentiment
from apps.utils.speech import _STT

class DiaryListCreateAPIView(ListCreateAPIView):
    queryset = Diary.objects.order_by('?')
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user
        voice_file_pk = request.data.get('voice_file', None)

        if voice_file_pk:
            directory = 'uploads/'
            directory += File.objects.get(id=voice_file_pk).name
            speech_text = _STT(directory)
            request.data['content'] = speech_text

            try:
                del request.data['title']
            except KeyError:
                pass

            sentiment = sample_analyze_sentiment(speech_text)
        else:
            sentiment = sample_analyze_sentiment(request.data.get('content'))

        request.data['score'] = sentiment[0]
        request.data['magnitude'] = sentiment[1]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DiaryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    lookup_url_kwarg = 'diary_pk'

