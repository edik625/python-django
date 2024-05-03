from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    data = models.IntegerField()
    location = models.CharField(max_length=30)

    def __str__(self) :
        return f"{self.title} will be held {self.data} "