# Generated by Django 2.0.7 on 2018-10-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20181020_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_item',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
