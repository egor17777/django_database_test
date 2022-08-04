from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path("book/<slug:slug_book>", views.get_book, name='book-url'),
    path('__debug__/', include('debug_toolbar.urls')),
]
