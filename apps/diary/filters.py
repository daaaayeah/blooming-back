import django_filters

from .models import Diary

class DiaryFilter(django_filters.FilterSet):

    class Meta:
        model = Diary
        fields = {
            'created_at': ['gte', 'lte']
        }