# Generated by Django 4.2.5 on 2023-09-13 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_product_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='date_added',
        ),
    ]