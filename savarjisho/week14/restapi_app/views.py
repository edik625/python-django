# from django.shortcuts import render
from rest_framework import APIVIew
# # Create your views here.
import io
from rest_framework.response import Response
# from .serializer import BookSerializer

# from .models import Book

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookAPIView(APIView):
    def get(delf,request):
        return Response