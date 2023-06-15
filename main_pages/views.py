from django.shortcuts import render
from .models import Collection, Card


def base(request):
    return render(request, "base.html")


def main_page(request):
    collections = Collection.objects.all()
    cards = Card.objects.select_related('product__product_color', 'product__product_material').all()
    context = {
        'collections': collections,
        'cards': cards,
    }
    return render(request, 'main_pages/main_page.html', context)

