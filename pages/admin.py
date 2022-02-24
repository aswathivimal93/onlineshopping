from unicodedata import category
from django.contrib import admin
from .models import Size, SubCategory, WelcomeSlides,Product,Discount,Category
# Register your models here.
admin.site.register(WelcomeSlides)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Size)