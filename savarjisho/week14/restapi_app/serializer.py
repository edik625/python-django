from rest_framework import serializers
from .models import Book

class BookSerializer(serilizer.ModelSerializer):
    class Meta:
        model = Book
        fielsd = "__all__"