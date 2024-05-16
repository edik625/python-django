from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data is not None:
                user = authenticate(request, username=data['username'], password = data['password'])
                login(request,user)
                return redirect('product_list')
            else:
                return HttpResponse('wrong input')
        else:
            redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'user/registrations.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')