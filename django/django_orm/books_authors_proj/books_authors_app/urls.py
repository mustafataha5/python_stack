from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('books',views.index_books),
    path('addBook',views.add_book),
    path('book/<int:id>',views.show_book),
    path("addAuthortoBook/<int:id>",views.add_author_to_book),
    path('authors/',views.index_authors),
    path('addAuthor',views.add_author),
    path('author/<int:id>',views.show_author),
    path('addBooktoAuthor/<int:id>',views.add_book_to_author),
]