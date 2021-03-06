# Generated by Django 3.1.2 on 2021-11-25 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_motorcycle_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motorcycle', to='main_app.client'),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='vin',
            field=models.CharField(max_length=17),
        ),
    ]
