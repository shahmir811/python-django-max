from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.
def index(request):
  books = Book.objects.all()
  return render(request, 'book_outlet/index.html', {
    "books": books
  })


def book_detail(request, book_id):

  # try:
  #   book = Book.objects.get(pk=book_id)
  
  # except:
  #   raise Http404()

  book = get_object_or_404(Book, pk=book_id)
  return render(request, 'book_outlet/book_detail.html', {
    "author": book.author,
    "is_bestselling": book.is_bestselling,
    "rating": book.rating,
    "title": book.title,
  })
  
