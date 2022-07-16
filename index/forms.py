from django.forms import DateTimeInput, ModelForm, TextInput, Textarea
from .models import bd


class IndexForm(ModelForm):
    class Meta:
        model = bd
        fields = ['title', 'contents', 'datatime']
        widgets = {
            "title":TextInput(attrs={
                'placeholder':'Название заметки'
            }),
            "contents": Textarea(attrs={
                'placeholder': 'Текст заметки',
            }),
            "datatime": DateTimeInput(attrs={
                'placeholder': 'Время публикации'
            }),
        }
