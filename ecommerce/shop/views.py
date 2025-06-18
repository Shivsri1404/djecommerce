from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Banner, FeaturedCategory, Slider, ContactUs, Product, Category, Users
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
        context = {"productObjs":productObjs, "CategoryObjs":CategoryObjs, "msg":"Products not found!!!"}
    except (KeyError, Product.DoesNotExist):
        context = {"msg":"Product not found!!!"}
    return render(request, "shop/shop.html", context)

def shopCategory(request, category_id):
    try:
        CategoryObjs = Category.objects.filter(child_categ_ids=category_id)
        productObjs = Product.objects.filter(category_id=category_id,published=True)
        context = {"CategoryObjs":CategoryObjs, "productObjs":productObjs, "msg":"No products found in this category!!!"}    
    except:
        context = {"msg":"Product not found!!!"}
    return render(request, "shop/shop.html", context)

from django.contrib.auth.models import User 
from django.contrib import messages
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if Users.objects.filter(username=username).exists():
            return render(request, 'shop/signup.html',{'msg':"Username already taken."})
        else:
            user = Users.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            # messages.success(request, "Account created successfully.")
            return redirect('shop:home')
    return render(request, 'shop/signup.html')

from django.contrib.auth import authenticate, login, logout

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:home')
        else:
            return render(request, 'shop/signin.html',{'msg':"Invalid credentials."})
    return render(request, 'shop/signin.html')

def logout_view(request):
    logout(request)
    return redirect('shop:home')

# from django.contrib.auth.decorators import login_required
# @login_required
# def dashboard_view(request):
#     return render(request, 'shop/dashboard.html')
