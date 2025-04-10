from django.contrib import admin
import users.models as models
# Register your models here.
admin.site.register([models.CustomUser, models.Client])