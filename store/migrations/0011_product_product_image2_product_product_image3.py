# Generated by Django 4.1.7 on 2023-02-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
