from django.shortcuts import render

from . models import Times
from .serializers import TimesSerializers
from rest_framework import viewsets

# Create your views here.

class TimesView(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializers
