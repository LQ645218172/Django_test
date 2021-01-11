from django.contrib import admin
from django.contrib import admin

from . import models
admin.site.register(models.Article)
admin.site.register(models.Reporter)
# Register your models here.
