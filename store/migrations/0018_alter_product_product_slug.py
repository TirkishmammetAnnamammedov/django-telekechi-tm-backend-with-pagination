# Generated by Django 4.0.5 on 2023-03-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_product_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(default=' '),
        ),
    ]
