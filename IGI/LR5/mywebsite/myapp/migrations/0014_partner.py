# Generated by Django 5.0.6 on 2024-09-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('site_url', models.URLField(default='https://doctorface.by/')),
                ('image_url', models.URLField(default='https://doctorface.by/upload/CAllcorp3Medc/303/73auzuayw1hh7elpf74bmd9nh8lu14jo.png')),
            ],
        ),
    ]
