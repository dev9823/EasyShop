# Generated by Django 4.2.6 on 2023-10-23 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_address_customer_remove_address_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='order',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='store.order'),
            preserve_default=False,
        ),
    ]
