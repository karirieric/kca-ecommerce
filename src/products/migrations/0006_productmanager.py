# Generated by Django 4.2 on 2023-04-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
