from django.shortcuts import render
from .models import bd

def index(request):
    return render(request, 'index/index.html', {'title':'Главная'})

def notes(request):
    all_text = bd.objects.all()
    return render(request, 'index/notes.html', {'title': 'Заметки', 'all': all_text,})
    
def add_notes(request):
    return render(request, 'index/add_notes.html', {'title': 'Добавление заметки'})
