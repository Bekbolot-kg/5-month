# Generated by Django 4.2.2 on 2023-07-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='product.color'),
        ),
    ]
