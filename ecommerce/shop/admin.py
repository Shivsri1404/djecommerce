from django.contrib import admin
from . models import Banner, Category, FeaturedCategory, Product, Slider
# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(FeaturedCategory)
admin.site.register(Product)
admin.site.register(Slider)