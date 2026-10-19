from django.urls import path
from author.views import author_page
from book.views import book_page
from order.views import order_page
from user.views import user_page

urlpatterns = [
    path('author/', author_page),
    path('book/', book_page),
    path('order/', order_page),
    path('user/', user_page),
]