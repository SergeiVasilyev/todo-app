from django.db import models
from django import forms

class Todolist(models.Model):
    todoitem = models.CharField(max_length=800)
    todoitem_fav = models.BooleanField()
    

    def __str__(self):
        return f"Todolist: {self.todoitem}"


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)