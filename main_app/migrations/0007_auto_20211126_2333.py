# Generated by Django 3.1.2 on 2021-11-26 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20211125_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='part',
            field=models.ForeignKey(default='No Parts', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='record', to='main_app.part'),
        ),
    ]