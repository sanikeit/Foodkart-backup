# Generated by Django 3.2.1 on 2021-06-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodkart', '0011_remove_addresses_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='total_price',
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(default='XXX', max_length=300),
        ),
    ]
