# Generated by Django 3.0.8 on 2021-03-08 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_cust_registration_table_lname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='sales_date',
        ),
    ]
