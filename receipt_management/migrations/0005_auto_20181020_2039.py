# Generated by Django 2.1.2 on 2018-10-20 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_management', '0004_auto_20181020_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptitem',
            name='receipt',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipt_item', to='receipt_management.Receipt'),
        ),
    ]
