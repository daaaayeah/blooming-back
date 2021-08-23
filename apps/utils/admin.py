from django.contrib import admin
from django.contrib.auth.models import Group

from apps.authentication.models import User
from apps.diary.models import Diary


admin.site.register(User)
admin.site.register(Diary)
admin.site.unregister(Group)
