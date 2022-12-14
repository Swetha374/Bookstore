from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,UpdateView,CreateView
from bookstoreapp import forms
from django.urls import reverse_lazy
from bookstoreapp.models import Books
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class SignUpView(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"Your account has been created")
        return super().form_valid(form)
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("login success..")
                print(user)
                return redirect("index")
            else:
                print("invalid user...")
                return render(request, "login.html",{"form":form})

class IndexView(TemplateView):
    template_name = "home.html"

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        form=forms.AddBookForm()
        return render(request,"add-book.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-book")
        else:
            return render(request,"add-book.html",{"form":form})

class ListBookView(View):
    def get(self,request,*args,**kwargs):
        form=forms.AddBookForm()
        book=Books.objects.all()
        return render(request,"list-books.html",{"book":book})

class DetailBookView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        return render(request,"book-details.html",{"book":book})

def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    return redirect("list-book")
class EditBookView(UpdateView):
    model=Books
    form_class = forms.EditBookForm
    template_name = "edit-book.html"
    pk_url_kwarg = "id"
    success_url =reverse_lazy("list-book")

    def form_valid(self, form):
        messages.success(self.request, "Book details has been changed")
        return super().form_valid(form)

# class EditBookView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         book=Books.objects.get(id=id)
#         form=forms.EditBookForm(instance=book)
#         return render(request,"edit-book.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         book = Books.objects.get(id=id)
#         form=forms.EditBookForm(request.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             redirect("list-book")
#         else:
#             return render(request, "list-books.html", {"form": form})
# class Cart_add_order(View):
#     def add_to_cart(request,*args,**kwargs):
#         id=kwargs.get("id")
#         book=Book.objects.get(id=id)

