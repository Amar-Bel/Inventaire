from django.db import models
from django.contrib.auth.models import User
# Create your models here.
category =(
    ('Stationary' , 'Stationary'),
    ('Electronics' , 'Electronics'),
    ('Food' , 'Food'),
)


class Products(models.Model):
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=20,choices=category)
    quantity=models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    Products = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order_quantity= models.PositiveBigIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Products} order by {self.staff}'

