from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) # blank=True savaldebulo ar iqneba rom eg veli sheivsos
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title