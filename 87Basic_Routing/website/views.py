from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>i am website</h1>")

def index1(requesr):
    return HttpResponse("<h2>This is the home page</h2>")
def index2(requesr):
    return HttpResponse("<h2>This is the about page</h2>")
def index3(requesr):
    return HttpResponse("<h2>This is the contact page</h2>")