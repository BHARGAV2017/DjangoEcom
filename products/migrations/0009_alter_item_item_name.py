# Generated by Django 4.1.4 on 2022-12-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_category_category_name_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]