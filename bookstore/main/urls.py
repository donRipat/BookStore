from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('test', views.test, name='test'),
    path('book/<int:book_id>', views.book_page, name='book'),
    path('user', views.user_page, name='user')
]
