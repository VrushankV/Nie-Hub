# Generated by Django 2.0.9 on 2018-11-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20181121_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='attachment_link',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
