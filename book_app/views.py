from django.shortcuts import get_object_or_404, render
from .models import Book, Author, Hero
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

def author(rquest):
    authors = Author.objects.all()

    return render(rquest, "book_app/all_authors.html", {'authors' : authors})

def get_author(request, id_author):
    author = get_object_or_404(Author, id = id_author)
     
    return render(request, "book_app/one_author.html",{"author" : author})

def all_heroes(rquest):
    heroes = Hero.objects.all()
    return render(rquest, "book_app/all_heroes.html", {'heroes' : heroes})

def get_hero(request, id_hero):
    hero = get_object_or_404(Hero, id = id_hero)
    return render(request, "book_app/one_hero.html",{"hero" : hero})