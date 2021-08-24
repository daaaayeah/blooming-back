from django.db import models
from django.contrib.auth import get_user_model


class File(models.Model):
    name = models.CharField(max_length=256)
    uploader = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
