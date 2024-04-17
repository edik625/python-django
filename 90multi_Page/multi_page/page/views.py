from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request, 'page/page.html')


def home_veb(request):
    return render(request, 'page/index.html')

def about_veb(request): 
    return render(request, 'page/index.html')

def contact_veb(request): 
    return render(request, 'page/index1.html')