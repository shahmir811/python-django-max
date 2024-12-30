from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.
def index(request):
  books = Book.objects.all().order_by('title') # get all the books from the database and order them by title
  num_books = books.count()
  avg_rating = books.aggregate(Avg('rating'))

  return render(request, 'book_outlet/index.html', {
    "books": books,
    "total_number_of_books": num_books,
    "average_rating": avg_rating['rating__avg'],
  })


def book_detail(request, slug):

  # try:
  #   book = Book.objects.get(slug=slug)
  
  # except:
  #   raise Http404()

  book = get_object_or_404(Book, slug=slug)
  return render(request, 'book_outlet/book_detail.html', {
    "author": book.author,
    "is_bestselling": book.is_bestselling,
    "rating": book.rating,
    "title": book.title,
  })
  
