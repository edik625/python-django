from django.urls import path
from .views import index1, index2

urlpatterns = [
    path("", index1) ,
    path("<int:id>", index2) ,
]
