# Generated by Django 4.2.6 on 2023-10-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_city_order_street_address_order_zipcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]