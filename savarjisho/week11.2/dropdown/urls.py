from django.urls import path
from .views import drop


urlpatterns = [
    path('' , drop) ,
]
