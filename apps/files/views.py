import os
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST as _400, HTTP_201_CREATED as _201
from rest_framework.parsers import MultiPartParser

from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage

from .models import File
from .serializers import FileSerializer

class FileListCreateAPIView(ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def create(self, *args, **kwargs):

        file = self.request.data.get('file')
        uploads = os.listdir(os.path.relpath('./uploads'))

        if file.name in uploads:
            return Response(
                {'message': 'File {} exists'.format(file.name)},
                status=_400)
        else:
            fs = FileSystemStorage('uploads')
            file_name = fs.save(file.name, file)
            serializer = self.get_serializer(data={'uploader': self.request.user, 'name': file.name})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=_201, headers=headers)

        