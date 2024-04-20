from django.shortcuts import render, redirect

# Create your views here.
def calculator(request):
    return render(request, 'calculate/index.html')

def add_veb(request,):
    if request.method == 'POST':
        number1 = request.POST.get('num1', '')
        number2 = request.POST.get('num2', '')
        add = int(number1) + int(number2)
        return render(request, 'calculate/add.html', {'number1':number1,'number2':number2, 'add': add})
    return render (request, 'calculate/calculator.html')

def subtract_veb(request):
    if request.method == 'POST':
        number1 = request.POST.get('num1', '')
        number2 = request.POST.get('num2', '')
        subtract = int(number1) - int(number2)
        return render(request, 'calculate/subtract.html', {'number1':number1,'number2':number2, 'subtract': subtract})
    return render (request, 'calculate/calculator.html')

def multiply_veb(request):
    if request.method == 'POST':
        number1 = request.POST.get('num1', '')
        number2 = request.POST.get('num2', '')
        multiply = int(number1) * int(number2)
        return render(request, 'calculate/multiply.html', {'number1':number1,'number2':number2, 'multiply': multiply})
    return render (request, 'calculate/calculator.html')

def divide_veb(request):
    if request.method == 'POST':
        number1 = request.POST.get('num1', '')
        number2 = request.POST.get('num2', '')
        divide = int(number1) / int(number2)
        return render(request, 'calculate/divide.html', {'number1':number1,'number2':number2, 'divide': divide})
    return render (request, 'calculate/calculator.html')