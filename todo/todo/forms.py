""" from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100) """

from django import forms
from .models import Todolist

class TodosForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['todoitem', 'todoitem_fav']
