# Generated by Django 3.0.8 on 2021-03-14 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20210314_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='cust_id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='cust_name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='purchase_rate',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='sales_date',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='sales_price',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='sup_name',
        ),
    ]
