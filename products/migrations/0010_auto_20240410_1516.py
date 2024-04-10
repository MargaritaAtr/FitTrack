# Generated by Django 3.2.24 on 2024-04-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productsize_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='productsize_stock',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='different_size',
            field=models.BooleanField(default=False),
        ),
    ]
