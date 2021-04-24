from django.db import models

# Create your models here.

class Spam(models.Model):
    email = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    tresc = models.TextField(blank=True, null = True)
    time  = models.TimeField(auto_now=False, auto_now_add=False)

