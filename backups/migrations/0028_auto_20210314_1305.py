# Generated by Django 3.0.8 on 2021-03-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_auto_20210314_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='p_name',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]
