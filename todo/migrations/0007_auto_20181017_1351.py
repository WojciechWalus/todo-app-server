# Generated by Django 2.1.2 on 2018-10-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_todoapps_canloginusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapps',
            name='canRequestActiveNotes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todonote',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
