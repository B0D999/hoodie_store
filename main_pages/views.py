from django.shortcuts import render


def base(request):
    return render(request, "main_pages/base.html")


def main_page(request):
    return render(request, "main_pages/main_page.html")
