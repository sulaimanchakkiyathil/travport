# Generated by Django 3.0.8 on 2021-03-23 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210323_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts_table',
            name='test1',
        ),
    ]
