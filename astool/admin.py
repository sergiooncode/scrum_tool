from django.contrib import admin

from .models import Task, Sprint

admin.site.register(Sprint)
admin.site.register(Task)
