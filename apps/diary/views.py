from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from django_filters.rest_framework import DjangoFilterBackend

from .models import Diary
from .serializers import DiarySerializer
from .filters import DiaryFilter

from apps.files.models import File
from apps.utils.language import sample_analyze_sentiment
from apps.utils.speech import _STT



class DiaryListCreateAPIView(ListCreateAPIView):
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DiaryFilter

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)

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
    lookup_url_kwarg = 'diary_pk'

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        request.data['author'] = request.user
        
        sentiment = sample_analyze_sentiment(request.data.get('content'))
        request.data['score'] = sentiment[0]
        request.data['magnitude'] = sentiment[1]

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DiaryLikeAPIView(UpdateAPIView):
    serializer_class = DiarySerializer
    lookup_url_kwarg = 'diary_pk'

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)

    def update(self, request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()

            if self.request.user in instance.like.all():
                return Response('This user already likes this diary.')
            else:
                instance._like(self.request.user)

            return Response('liked')

class DiaryUnlikeAPIView(UpdateAPIView):
    serializer_class = DiarySerializer
    lookup_url_kwarg = 'diary_pk'

    def get_queryset(self):
        return Diary.objects.filter(author=self.request.user)

    def update(self, request, *args, **kwargs):
            instance = self.get_object()

            if self.request.user in instance.like.all():
                instance._unlike(self.request.user)
            else:
                return Response('This user already unlikes this diary.')

            return Response('unliked')