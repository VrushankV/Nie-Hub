# Generated by Django 2.0.9 on 2018-11-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181108_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
