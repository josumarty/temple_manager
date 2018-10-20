# Generated by Django 2.1.2 on 2018-10-20 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('star', models.CharField(choices=[('a', '2'), ('b', '1')], default='1', max_length=20)),
                ('total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vazhipadu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='receiptitem',
            name='vazhipadu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='receipt_management.Vazhipadu'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_items',
            field=models.ManyToManyField(to='receipt_management.ReceiptItem'),
        ),
    ]
