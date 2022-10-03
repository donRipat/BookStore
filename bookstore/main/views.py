from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная', 'books': books})


def sign_in(request):
    return render(request, 'main/sign_in.html')


def sign_up(request):
    return render(request, 'main/sign_up.html')


def test(request):
    return render(request, 'main/test.html')


def about(request):
    return render(request, 'main/about.html')
