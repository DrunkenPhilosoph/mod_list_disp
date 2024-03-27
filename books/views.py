from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
import datetime

def books_view(request):
    books_date = Book.objects.all().order_by('-pub_date')
    context = {'books_date': books_date}
    template = 'C:/PythonProjects/dj-homeworks/databases/models_list_displaying/templates/books/books_list.html'
    return render(request, template, context)

def book_detail(request, year=None, month=None, day=None):
    date = datetime.date(year, month, day)
    books_date = Book.objects.all().filter(pub_date=date)
    previous_book = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()
    context = {'books_date': books_date, 'previous_book': previous_book, 'next_book': next_book}
    template = 'C:/PythonProjects/dj-homeworks/databases/models_list_displaying/templates/books/book.html'
    return render(request, template, context)