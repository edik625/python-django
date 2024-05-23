from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.categoryName
    
class Bid(models.Model):
    bid = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True, related_name='userbid')

    def __str__(self):
        return self.user.username

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    imageurl = models.URLField()
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True,null=True, related_name='pricebid')
    isactive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True,null=True, related_name='category')
    watvhlist = models.ManyToManyField(User, blank=True, related_name='watchlist')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True, related_name='usercomment')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True,null=True, related_name='listingcomment')
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.author.username} comment on {self.listing.title}"