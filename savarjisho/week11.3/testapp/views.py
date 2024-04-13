from django.shortcuts import render

def index(request):
    data = ['apple', 'banana', 'orange']
    return render(request, 'index.html', {'data': data})
# Create your views here.
