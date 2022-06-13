from django.shortcuts import render
from .models import bd

def index(request):
    return render(request, 'index/index.html')


def notes(request):
    contents = bd.objects.all()
    return render(request, 'index/notes.html', {'con': contents} )
    