from django.http import HttpResponse
from django.shortcuts import render

from .models import Todolist



# def index(request):
#    return HttpResponse("Hello World!")


def index(request):




    list_array = []
    #for list in Todolist.objects.all():
    #    line = f'<p>{list.id}. {list.todoitem}</p>'
    #    list_array.append(line)
    #linkkiteksti = ''.join(list_array)


    context = {
        'todos': Todolist.objects.all(),
    }
    return render(request, 'todo/index.html', context)



