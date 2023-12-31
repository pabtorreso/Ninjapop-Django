# Generated by Django 4.2.2 on 2023-06-25 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_imagen1_product_imagen2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen1',
            field=models.ImageField(default='default_image.png', upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='imagen2',
            field=models.ImageField(default='default_image.png', upload_to='product_images'),
        ),
    ]
