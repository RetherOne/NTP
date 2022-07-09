from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('notes/', views.notes, name='notes',),
    path('add_notes/', views.add_notes, name='add_notes',),
]
