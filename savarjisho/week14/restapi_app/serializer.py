from rest_framework import serializers # type: ignore
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'      # cxrilshi yvela info wamoigebs
        # fields = ('title', 'publicated_date')   # shesadzlebia calke