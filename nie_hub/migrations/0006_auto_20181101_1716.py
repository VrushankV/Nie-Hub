# Generated by Django 2.0.9 on 2018-11-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nie_hub', '0005_auto_20181101_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=10),
        ),
    ]