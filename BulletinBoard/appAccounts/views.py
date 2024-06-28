from django.shortcuts import render, redirect


def home_page(request):
    """
    Представление для главной страницы с приветственным сообщением.
    """
    return render(request, 'home.html', {})
