# Generated by Django 4.1.4 on 2022-12-20 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_is_palced_remove_order_payment_status_and_more'),
        ('products', '0002_remove_selleritem_seller_name_selleritem_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='selleritem',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='selleritem',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='SellerItem',
        ),
    ]
