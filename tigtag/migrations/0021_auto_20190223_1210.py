# Generated by Django 2.1.7 on 2019-02-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigtag', '0020_auto_20190223_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitinglist',
            name='customer',
        ),
        migrations.AddField(
            model_name='waitinglist',
            name='waiting_number',
            field=models.IntegerField(default=0),
        ),
    ]
