from django.contrib import admin
from .models import Bid,Category,Comment,Listing,User
# Register your models here.
admin.site.register([Bid,Category,Comment,Listing,User])