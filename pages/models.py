from tkinter import CASCADE
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User 

# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User_created", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    def __str__(self):
        return self.locality
class WelcomeSlides(models.Model):
    image_link=models.ImageField(null=True,blank=True,upload_to="slider_images/")
    caption=models.CharField(max_length=1500)

    def _str_(self):
        return self.image_link

class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=1500)
    category_image=models.ImageField(null=True,blank=True,upload_to="category_images/")

    def _str_(self):
        return self.name

class SubCategpory(models.Model):
    name=models.CharField(max_length=50)

class Discount(models.Model):
    name=models.CharField(max_length=500)
    desc=models.CharField(max_length=1500)

    def _str_(self):
        return self.name

class Size(models.Model):
    name=models.CharField(max_length=50,null=True)
    productCategory=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="productCategory")

    def _str_(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=500)
    desc=models.CharField(max_length=1500)
    price=models.FloatField()
    productcategory=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="ProductCategory")
    discount_name=models.ForeignKey(Discount,on_delete=models.CASCADE,verbose_name="discount")
    image_link1=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    image_link2=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    image_link3=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name

class ProductSizeMapping(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='products')
    size=models.ForeignKey(Size,on_delete=models.CASCADE,related_name='size')


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User_customer", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="Product_name", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name="Shipping_Address", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Pending"
        )
    