from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Collection, Card, Product
from django.urls import reverse
from django.core import serializers
from decimal import Decimal


def base(request):
    return render(request, "base.html")


def main_page(request):
    collections = Collection.objects.all()
    cards = Card.objects.select_related('product__product_color', 'product__product_material').all()
    context = {
        'collections': collections,
        'cards': cards,
        'current_collection': None,
    }
    return render(request, 'main_pages/main_page.html', context)


def search(request):
    query = request.GET.get('query')

    if query:
        products = Product.objects.filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()

    collections = Collection.objects.all()

    context = {
        'products': products,
        'active_link': 'main_page',
        'query': query,
        'collections': collections,
    }
    print(f'query = {query}')
    return render(request, 'main_pages/search.html', context)


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


def card(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    context = {'product': product}
    return render(request, 'main_pages/card.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    cart = request.session.get('cart', {})

    product_data = {
        'id': product.product_id,
        'name': product.name,
        'price': str(product.price),
    }

    cart[product_id] = product_data
    request.session['cart'] = cart

    return redirect('cart')


def cart(request):
    cart_items = request.session.get('cart', [])
    total_cost = sum(item['product'].product_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
    }

    return render(request, 'main_pages/cart.html', context)
