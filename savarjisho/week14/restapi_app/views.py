# from django.shortcuts import render
# from .serializer import BookSerializer
# from .models import Book
# from rest_framework.views import APIView
# from rest_framework import generics

# # # Create your views here.




# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
    # serializer_class = BookSerializer


from .models import Book
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .serializer import BookSerializer

class BookAPIView(APIView):
    def get(self, request):
        lst = Book.objects.all()
        return Response({'books':BookSerializer(lst, many = True).data})
    
    def post(self, request):
        New_book = Book.objects.create(
            title = request.data['title'],
            publicated_date = request.data['publicated_date'],
            author = request.data['author']
        )
        return  Response({'book': BookSerializer(New_book).data})