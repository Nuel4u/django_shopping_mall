# Generated by Django 2.2.9 on 2020-05-21 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200521_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='address_type',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='default',
        ),
    ]
