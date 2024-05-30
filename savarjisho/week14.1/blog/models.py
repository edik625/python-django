from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    publicashed_date = models.DateTimeField()

    def __str__(self):
        return self.title