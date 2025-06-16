from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import logging
_logger = logging.getLogger(__name__)

# Create your models here.
class Banner(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    banner_image = models.ImageField(upload_to="shop/banner", blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    category_image = models.ImageField(upload_to="shop/category", blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)
    parent_categ_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    child_categ_ids = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.name

class FeaturedCategory(models.Model):

    name = models.CharField(max_length=20, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)
    
    def __str__(self):
        return self.name
    # Override save method to set name field before saving
    def save(self, *args, **kwargs):
        # Copy category name into name field before saving
        if self.category_id:
            self.name = self.category_id.name
        super().save(*args, **kwargs)

    # Signal to update FeaturedCategory name when Category name changes
    @receiver(post_save, sender=Category)
    def update_featured_category_name(sender, instance, **kwargs):
        FeaturedCategory.objects.filter(category_id=instance).update(name=instance.name)


class Product(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default = 10.00)
    product_image = models.ImageField(upload_to="shop/product", blank=False, null=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)
    published = models.BooleanField(default=False)
    internal_ref = models.CharField(max_length=20, editable=False, unique=True)
    # Suggested code may be subject to a license. Learn more: ~LicenseLog:2622567868.
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    allow_out_of_stock = models.BooleanField(default=False)
    product_type = models.CharField(max_length=20, choices=[('storable', 'Storable'), ('consumable', 'Consumable')], default='storable')
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.internal_ref = self.name[:4]+"_"+str(random.randint(1000,9999))
        super().save(*args, **kwargs)

class Slider(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    slider_type = models.CharField(max_length=20, choices=[('new', 'NEW'), ('manual', 'Manual')], default='new')
    product_ids = models.ManyToManyField(Product, blank=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.slider_type == 'new':
            self.product_ids.set(Product.objects.filter(published=True).order_by('-create_date')[:5])

class ContactUs(models.Model):

    # Suggested code may be subject to a license. Learn more: ~LicenseLog:2641710650.
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=False, null=False)
    question = models.TextField(blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Users(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    password = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

class Address(models.Model):

    name = models.CharField(max_length=20, blank=False, null=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, null=False)
    street  = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=40, blank=False, null=False)
    zip = models.CharField(max_length=10, blank=False, null=False)
    state = models.CharField(max_length=40, blank=False, null=False)
    country = models.CharField(max_length=40, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    create_date = models.DateTimeField("Create Date",auto_now_add=True)

    def __str__(self):
        return f"{self.user_id.name} - {self.name}"
