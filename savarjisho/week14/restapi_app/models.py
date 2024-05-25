from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()


    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=100)
    publicated_date = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
