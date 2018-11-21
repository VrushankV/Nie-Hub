from django.shortcuts import render,redirect
from . import views
from django.urls import path

# Create your views here.
urlpatterns=[
	path('buy',views.buy,name="buy"),
	path('buyd',views.buyd,name="buyd"),
	path('sell',views.sell,name="sell"),
	path('transaction_books',views.transaction_books,name="transaction_books"),
	path('waiting_books',views.waiting_books,name="waiting_books"),
]
