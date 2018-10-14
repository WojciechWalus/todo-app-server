from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.TodoNote)
admin.site.register(models.TodoUser)
admin.site.register(models.TodoApps)
