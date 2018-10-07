# Generated by Django 2.0.7 on 2018-10-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_project_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='items',
        ),
        migrations.RemoveField(
            model_name='project_item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='project_item',
            name='project',
            field=models.ManyToManyField(to='products.Project'),
        ),
    ]
