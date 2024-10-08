# Generated by Django 5.0.6 on 2024-05-19 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_schedule_doctor_alter_plannedvisit_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.client')),
                ('promo_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.discount')),
                ('services', models.ManyToManyField(to='myapp.service')),
            ],
        ),
    ]
