from django.http import HttpResponse

# Create your views here.

def index1(request):
    return HttpResponse("<h1>This is website 'odd_or_even' </h1>")


def index2(request, id):
    if id % 2 == 0 :
        print (id//2)
        return HttpResponse("<h1> This number is even </h1>")
    if id % 2 == 1 :
        print(1)
        return HttpResponse("<h1> This number is odd </h1>")