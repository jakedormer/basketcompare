# Generated by Django 2.0.7 on 2018-08-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180828_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='merchants',
            field=models.ManyToManyField(to='products.Merchant'),
        ),
    ]
