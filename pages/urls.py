from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('product_details/<int:product_id>/',views.productDetails,name="product_details")
]