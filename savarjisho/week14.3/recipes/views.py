from rest_framework import viewsets
from .models import Shef, Recepe
from .serializers import ShefSerializer, RecepeSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
# Create your views here.

class shefViewset(viewsets.ModelViewSet):
    queryset = Shef.objects.all()
    serializer_class = ShefSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RecepeViewset(viewsets.ModelViewSet):
    queryset = Recepe.objects.all()
    serializer_class = RecepeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LoginViewSet(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({"error":"wrong Credentials"})