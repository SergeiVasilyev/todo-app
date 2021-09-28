from django.http import HttpResponse
from django.shortcuts import render
from .forms import ArticlesForm

from .models import Todolist

# def index(request):
#    return HttpResponse("Hello World!")


def index(request):
    form = ArticlesForm()
    context = {
        'todos': Todolist.objects.all(),
        'form': form
    }
    return render(request, 'todo/index.html', context)


