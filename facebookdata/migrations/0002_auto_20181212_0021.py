# Generated by Django 2.1.2 on 2018-12-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbpost',
            name='pmessage',
            field=models.TextField(max_length=600),
        ),
    ]
