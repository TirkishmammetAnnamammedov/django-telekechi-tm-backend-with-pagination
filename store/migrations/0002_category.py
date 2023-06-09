# Generated by Django 4.1.6 on 2023-02-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category')),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
