from django.urls import path
from .views import index ,start_app
urlpatterns = [
    path("",index),
    path("start/",start_app)
]