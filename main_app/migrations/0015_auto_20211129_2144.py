# Generated by Django 3.1.2 on 2021-11-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20211129_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['created_at']},
        ),
    ]
