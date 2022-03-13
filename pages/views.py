from traceback import print_exc
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from .models import WelcomeSlides,Category,Product

# Create your views here.
def index(request):
    sliderImages=WelcomeSlides.objects.all()
    ProductCategories=Category.objects.all()
    products=Product.objects.all()
    Products_kids=Product.objects.filter(productcategory=1)
    products_women=Product.objects.filter(productcategory=2)
   
    context={'sliderImages':sliderImages,
            'ProductCategories':ProductCategories,
             'products':products,
             'Products_kids':Products_kids,
             'products_women':products_women}
    
    return render(request,'index.html',context)

def productDetails(request,product_id):
    product=Product.objects.filter(id=product_id)
    for p in product:
     print("product is",p.price,p.name,p.image_link1)
    for p in product:
        relatedProducts=Product.objects.exclude(id=product_id).filter(is_active=True,productcategory=p.productcategory)
    context={
        'product':product,
        'relatedProducts':relatedProducts
    }
    return render(request,'store/product_details.html',context)