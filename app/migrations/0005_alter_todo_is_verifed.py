# Generated by Django 3.2.3 on 2021-09-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_is_active_todo_is_verifed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_verifed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]