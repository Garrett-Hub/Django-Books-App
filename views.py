from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q
from .models import Author, Book
from .forms import AuthorForm, BookForm
import requests
import json


# Home page for Books app
def books(request):
    return render(request, "home.html")


# Takes user to page where they can add an author to the database
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('viewAuthors')
    else:
        print(form.errors)
        messages.error(request, "Error")
    context = {'form': form}
    return render(request, "addAuthor.html", context)


# Takes user to page where they can add a book to the database
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('viewBooks')
    else:
        print(form.errors)
        messages.error(request, "Error")
    context = {'form': form}
    return render(request, "addBook.html", context)


# Shows a page with every author in the database, sorted by last name
def view_authors(request):
    authors = Author.objects.order_by("lastName")
    context = {"authors": authors}
    return render(request, "viewAuthors.html", context)


# Shows a page with every book in the database, sorted by title
def view_books(request):
    books_list = Book.objects.order_by("title")
    context = {"books_list": books_list}
    return render(request, "viewBooks.html", context)


# Shows a page where an book's details can be viewed and edited
def book_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Book, pk=pk)
    form = BookForm(data=request.POST or None, instance=item)
    # TODO: When trying to save changes with only blank spaces in a field, the error message is not
    #  displayed correctly on the page and the user is taken to a django debug page
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('viewBooks')
        else:
            print(form.errors)
            messages.error(request, "Error")
    else:
        return render(request, 'bookDetails.html', {'form': form})


# Shows a page where an author's details can be viewed and edited
def author_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Author, pk=pk)
    form = AuthorForm(data=request.POST or None, instance=item)
    # TODO: When trying to save changes with only blank spaces in a field, the error message is not
    #  displayed correctly on the page and the user is taken to a django debug page
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('viewAuthors')
        else:
            print(form.errors)
            messages.error(request, "Error")
    else:
        return render(request, 'authorDetails.html', {'form': form})


# Takes user to a page to confirm deletion of an author
def delete_author(request, pk):
    pk = int(pk)
    item = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        try:
            item.delete()
            return redirect('viewAuthors')
        except Exception as e:
            # TODO: Errors don't show correctly on delete page, but at least the user isn't taken
            #  to a django debug page when trying to delete a protected author.
            messages.error(request, "Error")
            print(e)
    context = {"item": item}
    return render(request, 'deleteAuthor.html', context)


# Takes user to a page to confirm deletion of an author
def delete_book(request, pk):
    pk = int(pk)
    item = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        try:
            item.delete()
            return redirect('viewBooks')
        except Exception as e:
            messages.error(request, "Error")
            print(e)
    context = {"item": item}
    return render(request, 'deleteBook.html', context)


# Searches book titles and sorts results alphabetically
class BooksView(ListView):
    model = Book
    template_name = 'searchResults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list.order_by("title")


# Search the Open Library API for title and author and displays results in a table
# with a link to the Open Library works page
def search_open_library(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        parameters = {
            "title": title,
            "author": author
        }
        response = requests.get("https://openlibrary.org/search.json", params=parameters)
        docs = response.json()['docs']
        context = {"docs": docs}
        return render(request, 'searchLibrary.html', context)
