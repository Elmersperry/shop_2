from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О магазине',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit',
    }
    return render(request, 'main/about.html', context)