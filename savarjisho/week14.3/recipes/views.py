from rest_framework import viewsets
from .models import Shef, Recepe
from .serializers import ShefSerializer, RecepeSerializer
# Create your views here.

class shefViewset(viewsets.ModelViewSet):
    queryset = Shef.objects.all()
    serializer_class = ShefSerializer


class RecepeViewset(viewsets.ModelViewSet):
    queryset = Recepe.objects.all()
    serializer_class = RecepeSerializer