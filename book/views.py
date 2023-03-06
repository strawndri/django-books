from django.shortcuts import render
from .utils import search_books
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')

def search(request):
    query = request.GET.get('q')
    if query:
        books = search_books(query)
    else:
        books = []
    context = {'books': books, 'query': query}
    return render(request, 'book/search.html', context)
