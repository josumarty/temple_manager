# Generated by Django 2.1.2 on 2018-10-20 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_management', '0002_auto_20181020_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptitem',
            name='receipt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receipt_item', to='receipt_management.Receipt'),
        ),
    ]