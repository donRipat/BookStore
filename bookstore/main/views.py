from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def sign_in(request):
    return render(request, 'main/sign_in.html')


def sign_up(request):
    return render(request, 'main/sign_up.html')


def test(request):
    return render(request, 'main/test.html')


def about(request):
    return render(request, 'main/about.html')
