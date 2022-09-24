from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=120)
    price=models.IntegerField(default=150)
    author=models.CharField(max_length=120)
    quantity=models.IntegerField(default=1)
    publisher=models.CharField(max_length=120)

    def __str__(self):
        return self.book_name

class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name=models.ForeignKey(Books,on_delete=models.CASCADE)
    qty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date=models.DateField(auto_now_add=True)
    options = (
        ("in-cart", "in-cart"),
        ("order-placed", "order-placed"),
        ("cancelled", "cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")