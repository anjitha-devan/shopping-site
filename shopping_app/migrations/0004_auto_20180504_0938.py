# Generated by Django 2.0.5 on 2018-05-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0003_itemdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='Upload_image',
            field=models.ImageField(upload_to='shopping_app/images'),
        ),
    ]