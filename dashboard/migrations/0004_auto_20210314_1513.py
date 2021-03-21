# Generated by Django 3.0.8 on 2021-03-14 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_cust_registration_table_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='cust_registration_table',
            name='passport_expiry',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cust_registration_table',
            name='uid',
            field=models.CharField(default=django.utils.timezone.now, max_length=36),
            preserve_default=False,
        ),
    ]
