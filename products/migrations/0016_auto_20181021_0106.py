# Generated by Django 2.0.7 on 2018-10-21 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_project_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_item',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Project'),
        ),
    ]