# Generated by Django 3.1 on 2020-10-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201011_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='draw',
            name='rotation',
            field=models.IntegerField(default=0),
        ),
    ]
