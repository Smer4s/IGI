# Generated by Django 5.0.6 on 2024-09-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_certificate_phone_certificate_website_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='print_url',
            field=models.URLField(null=True),
        ),
    ]
