# Generated by Django 3.0.8 on 2021-03-14 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_auto_20210314_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliers_table',
            name='sup_address',
        ),
        migrations.RemoveField(
            model_name='suppliers_table',
            name='sup_contact',
        ),
        migrations.RemoveField(
            model_name='suppliers_table',
            name='sup_contact2',
        ),
        migrations.RemoveField(
            model_name='suppliers_table',
            name='sup_email',
        ),
        migrations.RemoveField(
            model_name='suppliers_table',
            name='web',
        ),
    ]
