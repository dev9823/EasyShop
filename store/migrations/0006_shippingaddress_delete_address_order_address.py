# Generated by Django 4.2.6 on 2023-10-22 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='store.customer')),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='store.shippingaddress'),
            preserve_default=False,
        ),
    ]