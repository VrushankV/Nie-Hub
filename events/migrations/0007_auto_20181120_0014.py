# Generated by Django 2.0.9 on 2018-11-19 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181119_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction_items',
            name='buyer_id',
        ),
        migrations.RemoveField(
            model_name='transaction_items',
            name='item_details_id',
        ),
        migrations.DeleteModel(
            name='Transaction_items',
        ),
    ]
