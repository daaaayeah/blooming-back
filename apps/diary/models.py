from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Diary(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.today)
    content = models.TextField()

    def __str__(self):
        return self.author + self.created_at
