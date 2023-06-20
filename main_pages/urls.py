from django.urls import path
from . import views

app_name = 'main_pages'

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('base/', views.base, name="base"),
    path('collection/<str:collection_name>/', views.collection_view, name="collection_view"),
    path('search/', views.search, name='search'),
    path('card/<int:product_id>/', views.card, name='card'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/clear', views.clear_cart, name='clear_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('cart/buy/', views.buy_cart, name='buy_cart'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout2'),
    path('signup/', views.register_view, name='signup'),
    path('cart/delete/<int:product_id>/', views.delete_cart_item, name='delete_cart_item'),
]
