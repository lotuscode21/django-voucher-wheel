# Generated by Django 3.1 on 2020-10-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='draw',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
