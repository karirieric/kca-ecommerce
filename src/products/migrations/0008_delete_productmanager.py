# Generated by Django 4.2 on 2023-04-24 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_products_featured'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductManager',
        ),
    ]
