from django.db import transaction
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404, redirect
from .models import Collection, Card, Product, Profile
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, product_id=product_id)
    cart1 = request.session.get('cart', {})

    product_data = {
        'id': product.product_id,
        'name': product.product_name,
        'price': round(float(product.product_price), 2),
        'stock': product.stock,
    }

    cart1[product.product_id] = product_data
    request.session['cart'] = cart1

    print(request.session['cart'])

    return redirect('main_pages:cart')


def get_cart(request):
    if 'cart' in request.session:
        cart = request.session['cart']
    else:
        cart = {}

    return cart


def cart(request):
    cart = get_cart(request)
    total_cost = Decimal(0)
    for cart_item in cart.values():
        price = Decimal(cart_item['price'])
        stock = Decimal(cart_item['stock'])
        total_cost += price * stock

    if request.method == 'POST':
        for product_id, cart_item in cart.items():
            quantity_key = f"quantity_{product_id}"
            if quantity_key in request.POST:
                quantity = int(request.POST[quantity_key])
                cart_item['stock'] = quantity

    context = {
        'cart': cart,
        'total_cost': total_cost.quantize(Decimal('0.00')),
    }
    return render(request, 'main_pages/cart.html', context)


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('main_pages:cart')


def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        delete_item = request.POST.get('delete_item')
        if delete_item:
            cart.pop(delete_item, None)
        else:
            for key in request.POST:
                if key.startswith('quantity_'):
                    product_id = key.split('quantity_')[1]
                    quantity = int(request.POST[key])
                    cart_item = cart.get(product_id)
                    if cart_item:
                        cart_item['stock'] = quantity
                        if quantity <= 0:
                            del cart[product_id]
        request.session['cart'] = cart

    return redirect('main_pages:cart')


def buy_cart(request):
    if request.method == 'POST':
        cart = get_cart(request)
        with transaction.atomic():
            for product_id, cart_item in cart.items():
                quantity = int(request.POST.get('quantity_' + str(product_id), cart_item['stock']))
                if quantity > 0:
                    product = Product.objects.select_for_update().get(product_id=product_id)
                    if product.stock >= quantity:
                        product.stock -= quantity
                        product.save()

            clear_cart(request)

    return redirect('main_pages:cart')


def delete_cart_item(request, product_id):
    print(f'Deleting product with ID: {product_id}')
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
    return redirect('main_pages:cart')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Неправильный логин или пароль")
            return redirect('/login/')
    else:
        return render(request, 'main_pages/login.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        FIO = request.POST.get('full_name')
        address = request.POST.get('address')
        image = request.POST.get('picture')
        try:
            user_object = User.objects.create_user(username=username, password=password)
        except Exception as exc:
            return redirect('/signup/')
        profile_object = Profile.objects.create(user=user_object, FIO=FIO, address=address, image=image)
        profile_object.save()
        login(request, user_object)
        return redirect('/')
    else:
        return render(request, 'main_pages/signup.html')


def logout_view(request):
    logout(request)
    print('dddd')
    return redirect('/')
