# Generated by Django 5.0.6 on 2024-07-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_product_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(max_length=5000, unique=True, verbose_name='Изображение'),
        ),
    ]
