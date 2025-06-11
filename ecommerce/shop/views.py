from django.shortcuts import render
from django.http import HttpResponse
from .models import Banner
# Create your views here.
def home(request):
    bannerObjs = Banner.objects.all()
    # return HttpResponse("Hello shop")
    context = {"bannerObjs":bannerObjs}
    print(bannerObjs[1:])
    return render(request, "shop/home.html", context)

