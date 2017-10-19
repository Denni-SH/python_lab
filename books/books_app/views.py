from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import CategoryForm, AuthorForm, BookForm
from django.shortcuts import redirect


def index(request):
    m_list = Book.objects.all()
    context = {'books': m_list}
    return render(request, 'books_list.html', context)


def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'new_category.html', {'form': form})


def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'new_author.html', {'form': form})


def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'new_book.html', {'form': form})


def details(request, pk):
    book = get_object_or_404(Book, title=pk)
    return render(request, 'details.html', {'book': book})
