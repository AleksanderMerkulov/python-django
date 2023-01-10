from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, FilterForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news_add.html'

    # fields = ['title', 'anons', 'full_text', 'date']
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

    # form_class = ArticlesForm



def news_adder(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма содержит ошибку'


    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/news_add.html', data)


def filter(request):
    form = FilterForm()
    return render(request, 'news/filter.html', {'form': form})
