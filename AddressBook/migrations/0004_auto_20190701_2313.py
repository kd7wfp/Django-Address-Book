# Generated by Django 2.2.3 on 2019-07-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddressBook', '0003_auto_20190701_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]