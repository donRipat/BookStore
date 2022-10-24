from django.shortcuts import render
from .models import Book, Order


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
    sign = 'Полный каталог доступных книг ' + f'({len(newlist)} кн.)'
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
        search += f'({len(newlist)} кн.)'
    return render(request, 'main/index.html', {'title': 'Главная', 'books': strs, 'sign': sign, 'search': search})


def book_page(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'main/book_page.html', {'book': book})


# def logic (вынести сюда логику шапки и подвала)


def ordering(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'main/buy.html', {'book': book})


def success(request, book_id):
    this_book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        new_ord = Order.objects.create(book=this_book, phone_num=request.POST['phone'], address=request.POST['address'],
                                       hints=request.POST['hints'], price=this_book.price)
        new_ord.save()
        return render(request, 'main/taskfailedsuccessfully.html')
    else:
        pass


def conditions(request):
    return render(request, 'main/conditions.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})
