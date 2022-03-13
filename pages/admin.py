from unicodedata import category
from django.contrib import admin
from .models import Size,WelcomeSlides,Product,Discount,Category,Address,ProductSizeMapping,Cart,Order
# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display=('user' , 'locality' , 'city' ,'state')
    list_filter=('city', 'state')
    list_per_page=10
    search_fields=('locality', 'city', 'state')

class WelcomeSlidesAdmin(admin.ModelAdmin):
    list_display=('image_link' , 'caption')
    list_per_page=10
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','description','category_image')
    list_editable=('category_image',)
    list_filter=('name',)
    list_per_page=10
    list_search=('name',)
class DiscountAdmin(admin.ModelAdmin):
    list_display=('name','desc')
    list_per_page=10

class SizeAdmin(admin.ModelAdmin):
    list_display=('name','productCategory')
    list_editable=('productCategory',)

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','desc','productcategory','is_active','is_featured','image_link1','updated_at')
    list_editable = ('productcategory', 'is_active', 'is_featured')
    list_filter = ('productcategory', 'is_active', 'is_featured')
    list_per_page=10
    search_fields = ('name', 'category', 'desc')
class ProductSizeMappingAdmin(admin.ModelAdmin):
    list_display=('product','size')
    list_editable=('size',)
    list_filter=('product',)
    list_per_page=10
    search_fields=('name',)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')



admin.site.register(WelcomeSlides,WelcomeSlidesAdmin)    
admin.site.register(Address,AddressAdmin)  
admin.site.register(Category,CategoryAdmin)  
admin.site.register(Product,ProductAdmin)
admin.site.register(Discount,DiscountAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(ProductSizeMapping,ProductSizeMappingAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)