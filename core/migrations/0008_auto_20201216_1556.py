# Generated by Django 3.1.4 on 2020-12-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201215_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talantuser',
            name='cs_result',
            field=models.CharField(default=None, max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='talantuser',
            name='dota_result',
            field=models.CharField(default=None, max_length=2500, null=True),
        ),
    ]
