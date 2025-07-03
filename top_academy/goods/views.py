from django.shortcuts import render
from .models import Products, Categories

def catalog(request):
    goods = Products.objects.all()
    context = {
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, slug):
    # product = Products.objects.get(slug=slug)
    # context = {
    #     'product': product,
    # }
    return render(request, 'goods/product.html')