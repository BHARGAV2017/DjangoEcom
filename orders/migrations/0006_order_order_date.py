# Generated by Django 4.1.4 on 2022-12-23 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_checkout_order_item_order_ord_qty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2022, 12, 23)),
        ),
    ]
