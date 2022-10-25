from django.shortcuts import render
from .models import Book, Order, User


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
    username = 'Вы не вошли'
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
    return render(request, 'main/index.html', {'title': 'Главная', 'books': strs, 'sign': sign, 'search': search, 'username': username})


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


def sign_in(request):
    return render(request, 'main/sign_in.html')


def auth(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['password']
        try:
            user = User.objects.get(name=n)
            if user.password == p:
                books = Book.objects.all().order_by('-bbe_score')
                newlist = books
                strs = []
                for i in range(len(newlist)):
                    if i % 3 == 0:
                        strs.append([])
                    strs[i // 3].append(newlist[i])
                sign = 'Полный каталог доступных книг ' + f'({len(newlist)} кн.)'
                search = 'Вы вошли как пользователь ' + n
                return render(request, 'main/index.html', {'title': 'Главная', 'books': strs, 'sign': sign, 'search': search,
                                                           'username': n})
            else:
                return render(request, 'main/sign_in.html', {'wrong': 'Неправильный логин или пароль'})
        except Exception:
            return render(request, 'main/sign_in.html', {'wrong': 'Неправильный логин или пароль 2'})
    return render(request, 'main/sign_in.html', {'wrong': 'Что-то пошло не так :('})


def sign_up(request):
    return render(request, 'main/sign_up.html')


def signed(request):
    u = ''
    n = ''
    if request.method == 'POST':
        u = request.POST['name']
        p = request.POST['password']
        user = User.objects.create(name=u, password=p)
        user.save()
        return render(request, 'main/registrated.html')
    else:
        pass


def conditions(request):
    return render(request, 'main/conditions.html')


def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})
