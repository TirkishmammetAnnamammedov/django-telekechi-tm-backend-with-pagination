# Generated by Django 4.1.6 on 2023-02-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=70)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('phone_number', models.CharField(max_length=20)),
                ('product_address', models.CharField(max_length=100)),
                ('product_quantity', models.CharField(max_length=8)),
                ('about_product', models.TextField(blank=True)),
                ('english_product_name', models.CharField(blank=True, max_length=70)),
                ('russian_product_name', models.CharField(blank=True, max_length=70)),
                ('is_vip', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('product_slug', models.SlugField(default='')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', to_field='category_name')),
            ],
        ),
    ]