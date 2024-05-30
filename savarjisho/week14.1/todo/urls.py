from django.contrib import admin
from django.urls import path, include
from .views import TodoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todos', TodoView)


urlpatterns = [
    path('', include(router.urls)),
]