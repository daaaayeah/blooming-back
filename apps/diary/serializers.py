from rest_framework import serializers

from .models import Diary


class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'
        extra_kwargs = {
            'like': {'read_only': True},
        }
