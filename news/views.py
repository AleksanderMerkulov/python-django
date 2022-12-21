from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news':news})


def news_adder(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('main')
        else:
            error = 'Форма содержит ошибку'


    form = ArticlesForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'news/news_add.html', data)