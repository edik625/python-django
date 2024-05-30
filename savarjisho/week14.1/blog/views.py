from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Post
from .serializers import AuthorSerialaizer, PostSerializers
# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerialaizer


class PostViewsSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    