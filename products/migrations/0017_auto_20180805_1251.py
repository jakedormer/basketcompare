# Generated by Django 2.0.7 on 2018-08-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180801_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]