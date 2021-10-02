from django.http import HttpResponse
from django.shortcuts import render
from .forms import TodosForm
from django.shortcuts import render, redirect
from django import forms
from .models import Todolist

# def index(request):
#    return HttpResponse("Hello World!")


def index(request):
    form = TodosForm()
    context = {
        'todos': Todolist.objects.all(),
        'form': form
    }
    return render(request, 'todo/index.html', context)

def addpage(request):
    print('ADDING NEW DATA', request)
    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            print('REQUEST:: ', form.id.lists()) #????????
            #form.save()
            return redirect('home')
    else:
        form = TodosForm()
    return render(request, 'post/new/', {'form': form})



# def addpage(request):
#     print('ADDING NEW DATA', request)
#     if request.method == "POST":
#         form = TodosForm(request.POST)
#         if form.is_valid():
#             form = Todolist(request.POST)
#             print('REQUEST:: ', form.id) #????????
#             form.save()
#             return redirect('home')
#     else:
#         form = TodosForm()
#     return render(request, 'post/new/', {'form': form})

