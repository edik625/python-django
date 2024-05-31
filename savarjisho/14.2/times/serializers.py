from rest_framework import serializers
from .models import Times

class TimesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Times
        fields = "__all__"