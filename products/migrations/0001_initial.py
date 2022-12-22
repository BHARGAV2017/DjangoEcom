# Generated by Django 4.1.4 on 2022-12-15 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('price_per_item', models.IntegerField(default=0)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='SellerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(default='', max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('per_qty_price', models.IntegerField(default=0)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
        ),
    ]