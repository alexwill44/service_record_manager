# Generated by Django 3.1.2 on 2021-11-25 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20211125_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
    ]
