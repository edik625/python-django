from django.shortcuts import render, redirect
from .models import task
# Create your views here.
def todo_list(request):
    queriset = task.objects.all()
    return render(request, "todo_list.html", {'data': queriset})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get ('title')
        task.objects.create(title=title)
    return redirect('todo_list')

def delete_task(request, task_id):
    task.objects.filter(pk=task_id).delete()
    return redirect('todo_list')

def edit_task(request,task_id):
    tasks = task.objects.get(pk=task_id)
    tasks.completed = True
    tasks.save()
    return redirect('todo_list')