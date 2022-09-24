"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from bookstoreapp import views

urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("books/add",views.AddBookView.as_view(),name="add-book"),
    path("books/list",views.ListBookView.as_view(),name="list-book"),
    path("books/detail/<int:id>",views.DetailBookView.as_view(),name="detail-book"),
    path("books/delete/<int:id>",views.delete_book,name="delete-book"),
    path("books/edit/<int:id>",views.EditBookView.as_view(),name="edit-book"),
]