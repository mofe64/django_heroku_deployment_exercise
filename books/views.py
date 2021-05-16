from django.shortcuts import render
from .models import Book


# Create your views here.
def all_books(request):
    books = Book.objects.all();
    context = {
        'books': books
    }
    return render(request, 'books/allBooks.html', context)
