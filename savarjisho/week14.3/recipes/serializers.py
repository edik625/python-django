from rest_framework import serializers
from .models import Shef, Recepe


class ShefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shef
        fields = "__all__"


class RecepeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepe
        fields = "__all__"
