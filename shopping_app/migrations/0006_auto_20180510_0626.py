# Generated by Django 2.0.5 on 2018-05-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0005_auto_20180510_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='Product_name',
            field=models.TextField(max_length=25),
        ),
    ]
