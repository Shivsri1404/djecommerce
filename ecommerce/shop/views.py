from django.shortcuts import render
from django.http import HttpResponse
from .models import Banner, FeaturedCategory, Slider
# Create your views here.
def home(request):
    bannerObjs = Banner.objects.all()
    FeaturedCategoryObjs = FeaturedCategory.objects.all()
    sliderObjs = Slider.objects.all()
    # return HttpResponse("Hello shop")
    context = {"bannerObjs":bannerObjs,"FeaturedCategoryObjs":FeaturedCategoryObjs, "sliderObjs":sliderObjs}
    # print(bannerObjs[1:])
    return render(request, "shop/home.html", context)

