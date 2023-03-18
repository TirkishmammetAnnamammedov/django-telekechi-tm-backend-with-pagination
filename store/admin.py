from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserClient, ForgotPassword, TurkmenTelekechi, Category, Product

class UserClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'joined_date')

class ForgotPasswordAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'posted_date')

class TurkmenTelekechiAdmin(admin.ModelAdmin):
    list_display = ('addresses', 'telekechi_phone_numbers', 'logos',)
    prepopulated_fields = {'slug': ('addresses',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'joined_date', 'category_image',)
    prepopulated_fields = {'slug': ('category_name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'joined_date', 'product_adder', 'product_image',)
    prepopulated_fields = {'product_slug': ('product_name',)}

admin.site.register(UserClient, UserClientAdmin)
admin.site.register(ForgotPassword, ForgotPasswordAdmin)
admin.site.register(TurkmenTelekechi, TurkmenTelekechiAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)

