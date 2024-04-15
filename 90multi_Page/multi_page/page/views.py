from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request, 'page.html')


def home_veb(request):
    return render(request, 'index.html')

def about_veb(request): 
    return render(request, 'index.html')

def contact_veb(request): 
    return render(request, 'index.html')