from rest_framework import serializers
from .models import Author, Post


class AuthorSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","name","bio"]

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"