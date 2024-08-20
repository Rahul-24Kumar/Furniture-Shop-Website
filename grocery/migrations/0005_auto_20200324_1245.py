# Generated by Django 2.2.6 on 2020-03-24 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20200324_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grocery.Status'),
        ),
    ]
