# Generated by Django 3.1.4 on 2020-12-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201207_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talantuser',
            name='steam_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
