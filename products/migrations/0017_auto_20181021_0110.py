# Generated by Django 2.0.7 on 2018-10-21 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20181021_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_item',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Project'),
        ),
    ]
