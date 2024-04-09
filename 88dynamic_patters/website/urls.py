from django.urls import path
from .views import index, name

urlpatterns = [
    path("", index),
    path("<str:id>", name),
]
