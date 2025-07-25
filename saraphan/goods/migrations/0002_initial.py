# Generated by Django 5.2.2 on 2025-06-09 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='shopping_carted',
            field=models.ManyToManyField(related_name='in_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category'),
        ),
        migrations.AddField(
            model_name='goods',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.subcategory'),
        ),
    ]
