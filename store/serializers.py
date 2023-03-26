from rest_framework import serializers
from .models import UserClient, ForgotPassword, TurkmenTelekechi, Category, Product

class UserClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClient
        fields = ('id', 'phone_number', 'password', 'joined_date', 'password_encrypted')

        # extra_kwargs = {'password': {
        #     'write_only': True,
        #     'required': True
        # }}

class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgotPassword
        fields = '__all__'

class TurkmenTelekechiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurkmenTelekechi
        fields = ('id', 'addresses', 'telekechi_phone_numbers', 'logos', 'about_us')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_image', 'joined_date')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_adder', 'product_name','product_price', 'product_image', 'product_image2', 'product_image3', 'product_image4', 'product_image5', 'phone_number', 'product_address', 'product_quantity', 'about_product', 'english_product_name', 'russian_product_name', 'delivery', 'credit', 'is_vip', 'is_active', 'joined_date', 'product_category')
