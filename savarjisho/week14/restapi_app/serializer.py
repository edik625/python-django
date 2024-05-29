from rest_framework import serializers # type: ignore
from .models import Book
from rest_framework.renderers import JSONRenderer
import io


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'      # cxrilshi yvela info wamoigebs
#         # fields = ('title', 'publicated_date')   # shesadzlebia calke



class BookModel:
    def __init__ (self, title, publicated_date, author):
        self.title = title
        self.publicated_date = publicated_date
        self.author = author


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 255)
    publicated_date  = serializers.DateField()
    author = serializers.IntegerField()

def encode():
    model = BookModel("New Book", '2023-05-29', 2)
    model_serialized = BookSerializer(model)
    print(model_serialized.data, type(model_serialized.data))
    json = JSONRenderer().render(model_serialized.data)
    print(json)



