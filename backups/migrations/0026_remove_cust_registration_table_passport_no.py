# Generated by Django 3.0.8 on 2021-03-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_remove_cust_registration_table_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cust_registration_table',
            name='passport_no',
        ),
    ]
