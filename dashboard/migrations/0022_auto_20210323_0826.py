# Generated by Django 3.0.8 on 2021-03-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20210323_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts_table',
            name='ac_credit',
            field=models.IntegerField(null=True),
        ),
    ]