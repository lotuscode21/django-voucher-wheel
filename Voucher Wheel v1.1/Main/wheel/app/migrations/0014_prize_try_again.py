# Generated by Django 3.1 on 2020-10-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201014_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='try_again',
            field=models.BooleanField(default=False),
        ),
    ]
