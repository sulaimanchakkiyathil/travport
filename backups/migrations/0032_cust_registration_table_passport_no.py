# Generated by Django 3.0.8 on 2021-03-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0031_auto_20210314_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='cust_registration_table',
            name='passport_no',
            field=models.CharField(blank=True, max_length=24),
        ),
    ]
