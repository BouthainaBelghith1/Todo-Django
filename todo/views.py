from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    context = {'all_tasks':tasks,
               'task_form':form}
    return render(request, 'todo/index.html', context)

def about(request):
    return render(request, 'todo/about.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index')

def delete_completed(request):
    Task.objects.filter(completed=True).delete()
    return redirect('index')

def delete_all(request):
    Task.objects.all().delete()
    return redirect('index')