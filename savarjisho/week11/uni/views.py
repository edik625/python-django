from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    return HttpResponse("university")


# def index(request):
#     x = render_to_string("index.html")
#     return HttpResponse(x)


def myclass(request):
    data = {"first_name": "edo", "last_name": "turmanidze", "fruits": ["apple", "banana", "orange"],
            "fruit" : {"citrus": "orange", "red_fruit": "stobary"}}
    return render (request,"index.html",data)

def myclass2(request,id):
    if id > 20:
        return redirect ('reddir')
    return HttpResponse(f"<h1>{id} student is our university</h1>")


def test_redirect(request):
    return HttpResponse("test")