# Generated by Django 4.1.4 on 2022-12-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_item_qty'),
        ('orders', '0004_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='ord_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='order_amount',
            field=models.IntegerField(default=0),
        ),
    ]