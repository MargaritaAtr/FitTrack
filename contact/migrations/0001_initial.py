# Generated by Django 3.2.24 on 2024-04-20 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Contact Form',
                'verbose_name_plural': 'Contact Forms',
                'ordering': ['-date_submitted'],
            },
        ),
    ]
