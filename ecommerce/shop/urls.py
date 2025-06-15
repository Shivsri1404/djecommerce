from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.home, name='home'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('productDetail/<int:pk>', views.productDetailView.as_view(), name='productDetail'),
    path('category/<int:category_id>', views.category, name='category'),
    path('shop/', views.shop, name='shop'),
] 
