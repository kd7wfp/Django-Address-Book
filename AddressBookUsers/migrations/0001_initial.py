# Generated by Django 2.2.3 on 2019-07-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AB_User',
            fields=[
                ('username', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
