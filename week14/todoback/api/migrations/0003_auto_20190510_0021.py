# Generated by Django 2.0.13 on 2019-05-09 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190510_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='TaskList',
            new_name='tasklist',
        ),
    ]
