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
        'current_collection': None,  # Add this line to pass the current collection value
    }
    return render(request, 'main_pages/main_page.html', context)


def collection_view(request, collection_name):
    collection = Collection.objects.get(name=collection_name)
    cards = Card.objects.filter(collection=collection)
    collections = Collection.objects.all()
    context = {
        'collection': collection,
        'cards': cards,
        'collections': collections,
        'current_collection': collection_name,
    }
    return render(request, 'collection.html', context)
