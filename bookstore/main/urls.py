from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('book/<int:book_id>', views.book_page, name='book'),
    path('book/ordering/<int:book_id>', views.ordering, name='ordering'),
    path('conditions', views.conditions, name='cond'),
    path('book/ordering/<int:book_id>/success', views.success, name='success')
]
