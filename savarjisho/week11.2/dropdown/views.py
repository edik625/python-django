from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def drop(request):
    number = {i for i in range(5)}
    options = ['Select a category', 'Tecnology', 'Fasion', 'Food', 'Travel', 'Health', 'Education', 'Finance']
    return render(request, 'dropdown/index.html', {'options': options, 'numbers': number}) 