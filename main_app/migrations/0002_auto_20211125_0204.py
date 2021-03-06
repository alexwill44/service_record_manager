# Generated by Django 3.1.2 on 2021-11-25 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motocycle', to='main_app.client'),
        ),
        migrations.AlterField(
            model_name='record',
            name='part',
            field=models.ForeignKey(default='Part Removed', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='record', to='main_app.part'),
        ),
        migrations.AlterField(
            model_name='record',
            name='tech',
            field=models.ForeignKey(default='No Technician Assigned', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='record', to='main_app.tech'),
        ),
    ]
