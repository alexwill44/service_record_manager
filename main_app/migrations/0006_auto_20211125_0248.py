# Generated by Django 3.1.2 on 2021-11-25 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_auto_20211125_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motorcycle', to=settings.AUTH_USER_MODEL),
        ),
    ]
