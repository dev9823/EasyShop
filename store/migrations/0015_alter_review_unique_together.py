# Generated by Django 4.2.6 on 2023-10-29 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_order_payment_method'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'product')},
        ),
    ]
