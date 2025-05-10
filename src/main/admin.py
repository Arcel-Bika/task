from django.contrib import admin
from main.models import Task, CustomUser


admin.site.register(Task)
admin.site.register(CustomUser)