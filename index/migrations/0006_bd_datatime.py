# Generated by Django 4.0.6 on 2022-07-16 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_bd_contents_alter_bd_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd',
            name='datatime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
