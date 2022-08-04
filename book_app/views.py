from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
# Create your views here.


def index(request):
    #books = Book.objects.order_by(F('author').asc(nulls_last=True))
    books = Book.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(True),
        str_1=Value('sdasdasd'),
        new_rating=F('rating')+1,
        top_rating=F('rating')+F('year'),
    )
    agg = books.aggregate(Max('rating'), Min('rating'), Count('id'))
    return render(request, "book_app/all_book.html", {
        'books' : books,
        'agg' : agg
        })

def get_book(request, slug_book):
    book = get_object_or_404(Book, slug = slug_book)
     
    return render(request, "book_app/one_book.html",{"book" : book})