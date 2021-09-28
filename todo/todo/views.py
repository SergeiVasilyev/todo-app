from django.http import HttpResponse
from django.shortcuts import render
from .forms import TodosForm
from django.shortcuts import render, redirect, get_object_or_404

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

# def forms(request):
#     form = TodosForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'todo/index.html', context)


def addpage(request):
    print('ADDING NEW DATA')
    if request.method == 'POST':
        form = Todolist(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = Todolist()
    return render(request, 'post/new/', {'form': form})
