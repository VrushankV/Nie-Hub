# Generated by Django 2.0.9 on 2018-11-03 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nie_hub', '0007_auto_20181103_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('body', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField(null=True)),
                ('create_date', models.DateTimeField(null=True)),
                ('venue', models.CharField(max_length=30, null=True)),
                ('interested_count', models.IntegerField(blank=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nie_hub.User')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Shirts', 'Shirts'), ('Trousers', 'Trousers'), ('Caps', 'Caps'), ('Others', 'Others')], max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
            ],
        ),
    ]