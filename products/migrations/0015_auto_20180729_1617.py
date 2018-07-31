# Generated by Django 2.0.7 on 2018-07-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20180727_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
