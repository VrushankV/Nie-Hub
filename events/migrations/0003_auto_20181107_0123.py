# Generated by Django 2.0.9 on 2018-11-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181105_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_details',
            name='size',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
