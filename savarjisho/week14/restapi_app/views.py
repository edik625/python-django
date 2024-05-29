from django.shortcuts import render
from rest_framework import generics
# from rest_framework.views import APIView
# # Create your views here.
import io
# from rest_framework.response import Response
from .serializer import BookSerializer

from .models import Book

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

