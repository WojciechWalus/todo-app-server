# Generated by Django 2.1.1 on 2018-10-13 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('user_token', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='todonote',
            name='user',
            field=models.CharField(max_length=300),
        ),
    ]
