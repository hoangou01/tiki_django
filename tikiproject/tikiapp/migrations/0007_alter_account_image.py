# Generated by Django 4.1.7 on 2023-04-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tikiapp', '0006_remove_order_item_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
