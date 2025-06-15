from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Banner, FeaturedCategory, Slider, ContactUs, Product, Category
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

def category(request, category_id):
    try:
        categoryObj = Category.objects.get(id=category_id)
        productObjs = Product.objects.filter(category_id=category_id,published=True)
        context = {"categoryObj":categoryObj, "productObjs":productObjs}
    except (KeyError, Category.DoesNotExist):
        context = {"msg":"Product not found!!!"}
    return render(request, "shop/category.html", context)

def shop(request):
    try:
        productObjs = Product.objects.filter(published=True)
        CategoryObjs = Category.objects.filter(parent_categ_id=None)
        # print(CategoryObjs)
        context = {"productObjs":productObjs, "CategoryObjs":CategoryObjs}
    except (KeyError, Product.DoesNotExist):
        context = {"msg":"Product not found!!!"}
    return render(request, "shop/shop.html", context)

