# Generated by Django 4.0.4 on 2022-05-23 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aperitivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
