# Generated by Django 3.2.3 on 2021-09-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_todo_is_verifed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='edit',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
