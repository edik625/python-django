from django.db import models

# Create your models here.

class Times(models.Model):
    currentTime = models.DateTimeField()


    def __str__(self):
        return self.currentTime