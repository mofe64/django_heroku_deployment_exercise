from django.shortcuts import render
from books.models import Book


# Create your views here.

def home(request):
    featured_books = Book.objects.all().filter(is_featured=True)[:10]
    context = {
        "featured_books": featured_books
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
