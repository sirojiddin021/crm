from django.contrib import admin
import tasks.models as models
# Register your models here.
admin.site.register(models.Task)