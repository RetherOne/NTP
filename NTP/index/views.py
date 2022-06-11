from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')


def notes(request):
    return render(request, 'index/notes.html')
