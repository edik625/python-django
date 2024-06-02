from django.db import models

# Create your models here.
class Shef(models.Model):
    name = models.CharField(max_length=100)
    spcialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recepe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    chef = models.ForeignKey(Shef,on_delete = models.CASCADE)

    def __str__(self):
        return self.title