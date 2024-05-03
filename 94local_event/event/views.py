from django.shortcuts import render, redirect
from .models import Event
# Create your views here.
def index(request):
    data = Event.objects.all()
    return render(request,'index.html',{'data':data})

def event_info(request,id):
    event = Event.objects.get(title=id)
    return render(request,'event_info.html', {'event':event})

def add_event(request):
    if request.method == 'POST':
        new_event = Event(
        title = request.POST.get('title'),
        description = request.POST.get('description'),
        data = request.POST.get('data'),
        location =  request.POST.get('location'),
        )
        new_event.save()
        return redirect('index')
    return render(request, 'add_event.html')

def delete_event(request,title):
    event = Event.objects.get(id=title)
    event.delete()
    return redirect('index')


def edit_event(request,title):
    if request.method == 'POST':
        event = Event.objects.get(title=title) 
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.data = request.POST.get('data')
        event.location =  request.POST.get('location')
        event.save()
        return redirect('index')
    return render(request,'edit_event.html')