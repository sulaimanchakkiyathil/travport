# Generated by Django 3.0.8 on 2021-03-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20210314_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='cust_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
