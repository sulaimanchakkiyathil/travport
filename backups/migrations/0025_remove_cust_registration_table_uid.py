# Generated by Django 3.0.8 on 2021-03-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20210314_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cust_registration_table',
            name='uid',
        ),
    ]
