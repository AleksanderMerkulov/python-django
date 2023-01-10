from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets={
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
        }


class FilterForm(forms.Form):
    date = forms.DateTimeField()
    name = forms.CharField(max_length=255)
    check = forms.BooleanField()
