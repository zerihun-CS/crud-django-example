# Generated by Django 4.2.6 on 2023-10-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_products_exp_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='ProductCategory',
            new_name='productCategory',
        ),
    ]