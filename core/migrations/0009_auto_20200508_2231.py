# Generated by Django 2.2.9 on 2020-05-08 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='apartment_address',
            new_name='appartment_address',
        ),
    ]
