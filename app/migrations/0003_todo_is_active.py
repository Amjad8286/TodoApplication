# Generated by Django 3.2.3 on 2021-09-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_deleteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
