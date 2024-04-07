from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate_from(request):
    return HttpResponse("""                   
    <form action="result" method="get">  
        <input type="number" name="num1" placeholder="Enter first name">
        <input type="number" name="num2" placeholder="Enter second name">                
        <input type="submit" value="calculate">
    </form>
""")

def multiply(request,num1,num2):
    result = num1 * num2
    return HttpResponse(f"<h1>{num1}*{num2} = {result}<h1>")

def calculate_result(request):
    if "num1" in request.GET and "num2" in request.GET :
        num1 = int(request.GET["num1"])
        num2 = int(request.GET["num2"])
        result = num1 * num2 
        return HttpResponse(f"Yours result are {result}")
    else:
         return HttpResponse(f"wrongs input")
    
def login_form(request):
    return HttpResponse("""                   
    <form action="login">  
        <input type="text" name="user" placeholder="User">
        <input type="text" name="password" placeholder="Password">                
        <input type="submit" value="calculate">
    </form>
""")
def login(request):
    register_user = "Admin"
    register_pass = "123456"
    if "user" in request.GET and "password" in request.GET:
        user = request.GET["user"]
        password = request.GET["password"]
        if register_user == user and register_pass == password:
            return HttpResponse("Hellow")
        else:
            return HttpResponse("wrong password")


def calculate_form(request):
    return HttpResponse("""                   
    <form action="calculate_form/result" method="get">  
        <input type="number" name="num1" placeholder="Enter first name">
        <input type="number" name="num2" placeholder="Enter second name">                
        <input type="submit" value="calculate">
    </form>
""")