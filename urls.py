from django.urls import path
from . import views
from .views import BooksView

urlpatterns = [
    path('books/', views.books, name="books"),
    path('addAuthor/', views.add_author, name="addAuthor"),
    path('addBook/', views.add_book, name="addBook"),
    path('viewAuthors/', views.view_authors, name="viewAuthors"),
    path('viewBooks/', views.view_books, name="viewBooks"),
    path('search/', BooksView.as_view(), name="search_results"),
    path('<int:pk>/bookDetails/', views.book_details, name="bookDetails"),
    path('<int:pk>/authorDetails/', views.author_details, name="authorDetails"),
    path('<int:pk>/deleteAuthor/', views.delete_author, name="deleteAuthor"),
    path('<int:pk>/deleteBook/', views.delete_book, name="deleteBook"),
    path('searchLibrary/', views.search_open_library, name="searchLibrary")
]