from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .models import bd
from .forms import IndexForm
# from datetime import *


def index(request, now=datetime.datetime.now()):
    return render(request, 'index/index.html', {
        'title':'Главная', 'time':now, 
    })


def notes(request, now=datetime.datetime.now()):
    all_text = bd.objects.all()
    return render(request, 'index/notes.html', {
        'title': 'Заметки', 'all': all_text, 'time': now, 
        })
    

def add_notes(request, now=datetime.datetime.now()):
    
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')

    return render(request, 'index/add_notes.html', {
        'title': 'Добавление заметки',
        'time': now,
        'form': IndexForm,
        })
