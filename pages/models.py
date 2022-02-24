from tkinter import CASCADE
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import date,datetime

# Create your models here.
class WelcomeSlides(models.Model):
    image_link=models.ImageField(null=True,blank=True,upload_to="slider_images/")
    caption=models.CharField(max_length=1500)
class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=1500)
    category_image=models.ImageField(null=True,blank=True,upload_to="category_images/")
class SubCategory(models.Model):
    name=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    subcategory_image=models.ImageField(null=True,blank=True,upload_to="subcategory_images/")
class Discount(models.Model):
    name=models.CharField(max_length=500)
    desc=models.CharField(max_length=1500)
class Size(models.Model):
    name=models.CharField(max_length=50,null=True)

class Product(models.Model):
    name=models.CharField(max_length=500)
    desc=models.CharField(max_length=1500)
    price=models.FloatField()
    subCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="subCategory")
    size=models.ForeignKey(Size,on_delete=models.CASCADE,related_name="size")
    discount_name=models.ForeignKey(Discount,on_delete=models.CASCADE,related_name="discount")
    image_link1=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    image_link2=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    image_link3=models.ImageField(null=True,blank=True,upload_to="Product_images/")
    created_at=models.DateField(blank=False)