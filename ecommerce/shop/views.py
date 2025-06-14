from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Banner, FeaturedCategory, Slider, ContactUs, Product
# from .forms import ContactUsForm
from django.urls import reverse
from django.views import generic



# Create your views here.
def home(request):
    bannerObjs = Banner.objects.all()
    FeaturedCategoryObjs = FeaturedCategory.objects.all()
    sliderObjs = Slider.objects.all()
    # return HttpResponse("Hello shop")
    context = {"bannerObjs":bannerObjs,"FeaturedCategoryObjs":FeaturedCategoryObjs, "sliderObjs":sliderObjs}
    # print(bannerObjs[1:])
    return render(request, "shop/home.html", context)

# def contactUs(request):
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("shop:contactUs"))
#     else:
#         form = ContactUsForm()
#     return render(request, 'shop/contactus.html', {'form': form})

def contactUs(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        question = request.POST.get('question')

        # Save to model
        ContactUs.objects.create(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            question=question
        )
        return HttpResponseRedirect(reverse("shop:contactUs"))

    return render(request, 'shop/contactus.html')
    
class productDetailView(generic.DetailView):
    model = Product
    template_name = "shop/productDetail.html"

    # return render(request, "shop/productDetail.html")