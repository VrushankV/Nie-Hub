# Generated by Django 2.0.9 on 2018-10-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nie_hub', '0003_auto_20181012_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
