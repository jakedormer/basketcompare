# Generated by Django 2.0.7 on 2018-07-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180727_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
