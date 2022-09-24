from django import forms
from django.contrib.auth.models import User
from bookstoreapp.models import Books

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "password"
        ]
        widgets={
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=[
            "book_name",
            "author",
            "price",
            "quantity",
            "publisher",
        ]
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "publisher": forms.TextInput(attrs={"class": "form-control"}),
        }

class EditBookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"