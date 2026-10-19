from django.shortcuts import render

def book_page(request):
    return render(request, 'book.html')