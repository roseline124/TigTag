# Generated by Django 2.1.7 on 2019-02-22 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigtag', '0014_remove_waitinglist_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waitinglist',
            name='waiting_number',
        ),
    ]
