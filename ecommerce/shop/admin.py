from django.contrib import admin
from . models import Banner, Category, FeaturedCategory, Product, Slider, ContactUs
# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(FeaturedCategory)
admin.site.register(Product)
admin.site.register(Slider)
admin.site.register(ContactUs)