# Generated by Django 4.2.6 on 2023-10-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_order_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('P', 'Paypal'), ('C', 'Card')], default='', max_length=1),
        ),
    ]
