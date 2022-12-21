# Generated by Django 4.1.4 on 2022-12-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('1', 'admin'), ('2', 'buyers'), ('3', 'sellers')], max_length=50),
        ),
    ]
