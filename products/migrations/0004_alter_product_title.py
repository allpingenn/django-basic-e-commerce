# Generated by Django 4.2.2 on 2023-06-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(max_length=400),
        ),
    ]