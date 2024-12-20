from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import BookForm
from .models import Book
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')







# Create your views here.
