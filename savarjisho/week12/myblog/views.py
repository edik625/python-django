from django.shortcuts import render

# Create your views here.
from.models import blog

def index(request):
    data = blog.objects.all()
    return render (request,'index.html', {'data':data} )