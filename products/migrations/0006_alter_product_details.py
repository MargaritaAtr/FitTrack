# Generated by Django 3.2.24 on 2024-04-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_special_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=360),
        ),
    ]