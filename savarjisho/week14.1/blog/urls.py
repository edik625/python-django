from django.contrib import admin
from django.urls import path, include
from .views import AuthorViewSet, PostViewsSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewsSet)


urlpatterns = [
    path('', include(router.urls)),
]