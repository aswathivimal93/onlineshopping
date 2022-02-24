from traceback import print_exc
from django.shortcuts import render
from .models import WelcomeSlides

# Create your views here.
def index(request):
    sliderImages=WelcomeSlides.objects.all()
    print_exc
    return render(request,'index.html',{'sliderImages':sliderImages})