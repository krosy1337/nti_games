# Generated by Django 3.1.4 on 2020-12-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201214_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talantuser',
            name='steam_id',
            field=models.BigIntegerField(default=None, null=True),
        ),
    ]
