# Generated by Django 2.1 on 2019-01-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookdata', '0005_auto_20190103_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbpost',
            name='pshare',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fbpost',
            name='pview',
            field=models.IntegerField(),
        ),
    ]
