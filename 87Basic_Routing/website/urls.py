from django.urls import path
from .views import index,index1,index2,index3

urlpatterns = [
    path("",index),
    path("home/",index1),
    path("about/",index2),
    path("contact/",index3)
]
