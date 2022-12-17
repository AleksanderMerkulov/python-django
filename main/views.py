from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main/main.html')


def about(request):
    data = {
        'title':'О нашем сайте',
        'content':'Мы такие зайки-лапочки'
    }
    return render(request, 'main/about.html', data)
