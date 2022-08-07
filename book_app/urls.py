from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('author', views.author),
    path('heroes', views.all_heroes),
    path('hero/<int:id_hero>', views.get_hero, name='hero-url'),
    path('author/<int:id_author>', views.get_author, name='author-url'),
    path("book/<slug:slug_book>", views.get_book, name='book-url'),
    path('__debug__/', include('debug_toolbar.urls')),
]
