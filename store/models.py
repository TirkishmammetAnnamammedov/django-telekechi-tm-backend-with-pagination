from django.db import models

class UserClient(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    password_encrypted = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = '2. Clients'

class ForgotPassword(models.Model):
    phone_number = models.CharField(max_length=15)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name_plural = '3. Forgot passwords'

class TurkmenTelekechi(models.Model):
    addresses = models.CharField(max_length=200, null =True)
    telekechi_phone_numbers = models.CharField(max_length=20)
    logos = models.ImageField(upload_to='logos', blank=True)
    about_us = models.TextField(blank=True)
    emails = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.telekechi_phone_numbers
    
    class Meta:
        verbose_name_plural = '1. Main site informations'

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_image = models.ImageField(upload_to='category', blank = True, null = True)
    joined_date = models.DateField(auto_now_add = True)
    slug = models.SlugField(default='category', null=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = '4. Categories'

class Product(models.Model):
    product_adder = models.ForeignKey(UserClient, on_delete=models.CASCADE, related_name='added_products', to_field='phone_number')
    product_name = models.CharField(max_length=70)
    product_price = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to='product', blank = True, null=True)
    product_image2 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image3 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image4 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image5 = models.ImageField(upload_to='product', blank = True, null=True)
    phone_number = models.CharField(max_length=20)
    product_address = models.CharField(max_length=100)
    product_quantity = models.CharField(max_length=8)
    about_product = models.TextField(blank = True)
    english_product_name = models.CharField(max_length=70, blank=True)
    russian_product_name = models.CharField(max_length=70, blank=True)
    is_vip = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    joined_date = models.DateField(auto_now_add=True)
    delivery = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    product_category = models.ForeignKey(Category, to_field='category_name', on_delete=models.CASCADE)
    product_slug = models.SlugField(default='onum', null=False)

    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name_plural = '5. Products'
