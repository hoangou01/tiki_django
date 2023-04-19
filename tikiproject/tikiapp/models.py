from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.conf import  settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Account (AbstractUser):

    image = models.CharField( max_length=300 ,default=None , null=True)
    address = models.CharField(max_length=80 , null=True)
    gender = models.CharField(max_length=20, null=True)
    DOB = models.DateField(null=True)
    description = RichTextField(null=True)
    phone = models.CharField(max_length=20, null=True, unique=True)
    is_seller = models.BooleanField(default=False,null=True)
    is_customer = models.BooleanField(default=False , null=True)
    # is_active = models.BooleanField(default=True , null=True)
    is_official = models.BooleanField(default= False , null=True)
    def __str__(self):
        return self.username

# class Customer (models.Model):
#
#     fullname = models.CharField(max_length=45 , null=False)
#     address = models.CharField(max_length=80 , null=False)
#     gender = models.CharField(max_length=20 , null=True)
#     DOB = models.DateField()
#     account = models.OneToOneField(Account , related_name='customer_set', on_delete=models.RESTRICT , null=False)
#     def __str__(self):
#         return self.fullname
# class Seller (models.Model):
#     description = RichTextField(null=True)
#     name = models.CharField(max_length=45 , null=False , unique=True)
#     phone = models.CharField(max_length=20 , null=True , unique=True)
#     address = models.CharField(max_length=45 , null=True)
#     is_official = models.BooleanField(default=False)
#     account = models.OneToOneField(Account ,  related_name='seller_set', on_delete=models.RESTRICT , null=False)
#     def __str__(self):
#         return self.name


class Category (models.Model):

    categoryname = models.CharField(max_length=45 , null=False , unique=True)
    image = models.ImageField(upload_to='Category/%Y/%m', null=True, blank=True )
    def __str__(self):
        return self.categoryname
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/static%s" width="50px" height="50px" />' % (self.image.url))
    image.short_description = 'Image'
#
class Product (models.Model):
    name = models.CharField(max_length=45 , null=False)
    base_price = models.DecimalField(max_digits=9 , decimal_places=0)
    product_sku = models.CharField(max_length=45 , null=True)
    quantity = models.IntegerField(null=False)
    salable_quantity = models.IntegerField(null=False)
    discount = models.IntegerField(null=True)
    image = models.ImageField(upload_to='Product/%Y/%m', default=None , null=True)
    description = RichTextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='product_set', on_delete=models.SET_NULL , null=True)
    is_active = models.BooleanField(default=False)
    seller = models.ForeignKey(Account ,related_name= 'product_seller_set' , on_delete=models.RESTRICT , null=False)
    account = models.ManyToManyField(Account, related_name='evaluate_set', through='Evaluate')
    def __str__(self):
        return self.name



class Cart (models.Model):
    total = models.DecimalField(max_digits=9 , decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account , on_delete=models.RESTRICT , null=False)
    product = models.ManyToManyField(Product , related_name='cart' , through='Cart_item')

class Cart_item (models.Model):
    quantity = models.IntegerField(null=False)
    cart = models.ForeignKey(Cart ,related_name='cart_item', on_delete=models.RESTRICT , null=False)
    product = models.ForeignKey(Product ,related_name='cart_item', on_delete=models.RESTRICT , null=False)

class Evaluate (models.Model):

    content = models.TextField(max_length=200 , null=False)
    rate = models.IntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account , related_name='evaluate' , on_delete=models.RESTRICT , null=False)
    product = models.ForeignKey(Product , related_name='evaluate' , on_delete=models.RESTRICT , null=False)
    def __str__(self):
        return self.content
class Order (models.Model):
    address_ship = models.CharField(max_length=100 , null=False)
    total = models.DecimalField(max_digits=9 , decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=40 , null=False)
    account = models.ForeignKey(Account , on_delete=models.RESTRICT , null=False)
    is_active = models.BooleanField(default=True)
    product = models.ManyToManyField(Product , related_name='order' , through='Order_item')
class Order_item (models.Model):
    quantity = models.IntegerField(null=False)
    product = models.ForeignKey(Product , related_name='order_item' , on_delete=models.RESTRICT , null=False)
    order = models.ForeignKey(Order , related_name='order_item' , on_delete=models.RESTRICT , null=False)
class Payment(models.Model):
    status = models.CharField(max_length=45 , null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    process = models.CharField(max_length=45 , null=True)
    order = models.ForeignKey(Order , on_delete=models.RESTRICT , null=False)



