from django.shortcuts import render

# Create your views here.
def index2(request):
    data = ['home', 'about',]
    return render(request, 'index1.html', {'data': data})