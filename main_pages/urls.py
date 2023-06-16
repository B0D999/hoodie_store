from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('base/', views.base, name="base"),
    path('collection/<str:collection_name>/', views.collection_view, name="collection_view"),
]
