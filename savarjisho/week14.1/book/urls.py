from django.contrib import admin
from django.urls import path, include
from .views import BookView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookView)


urlpatterns = [
    path('', include(router.urls)),
]