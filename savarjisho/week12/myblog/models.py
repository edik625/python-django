from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=50)

