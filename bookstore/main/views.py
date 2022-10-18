from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-bbe_score')
    newlist = []
    title = ''
    author = ''
    genre = ''
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
    for b in books:
        if title in b.title and genre in b.genres and author in b.author:
            newlist.append(b)
    strs = []
    for i in range(len(newlist)):
        if i % 3 == 0:
            strs.append([])
        strs[i // 3].append(newlist[i])
    print(strs)
    sign = 'Главная'
    search = ''
    if title != '' or author != '' or genre != '':
        sign = ''
        search = 'Результаты поиска '
        if title != '':
            search += f'в названиях: "{title}" '
        if author != '':
            search += f'среди авторов: "{author}" '
        if genre != '':
            search += f'среди жанров: "{genre}" '
        search += f'({len(newlist)})'
    return render(request, 'main/index.html', {'title': 'Главная', 'books': strs, 'sign': sign, 'search': search})


def book_page(request, book_id):
    book = get_book_by_id(book_id)
    return render(request, 'main/book_page.html', {'book_page': book_page, 'book': book})


#def logic (вынести сюда логику шапки и подвала)


def get_book_by_id(book_id):
    books = Book.objects.all()
    book = Book.objects.all().first
    for b in books:
        if b.id == book_id:
            book = b
    return book


def user_page(request):
    return render(request, 'main/user_page.html', {'title': 'Пользователь'})


def sign_in(request):
    return render(request, 'main/sign_in.html')


def sign_up(request):
    return render(request, 'main/sign_up.html')


def test(request):
    return render(request, 'main/test.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})
