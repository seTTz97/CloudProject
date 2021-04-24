from django.contrib import admin

# Register your models here.

from .models import Spam

admin.site.register(Spam)
