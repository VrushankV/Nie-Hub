# Generated by Django 2.0.9 on 2018-11-21 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20181121_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='links',
        ),
    ]