# Generated by Django 2.0.9 on 2018-11-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_transaction_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='interested_count',
        ),
    ]