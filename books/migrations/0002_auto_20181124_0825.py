from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_books',
            name='buyer_id1',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_id1', to='nie_hub.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction_books',
            name='owner_id1',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='owner_id1', to='nie_hub.User'),
            preserve_default=False,
        ),
    ]
