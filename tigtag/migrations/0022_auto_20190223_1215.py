# Generated by Django 2.1.7 on 2019-02-23 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigtag', '0021_auto_20190223_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waitinglist',
            old_name='waiting_number',
            new_name='customer_id',
        ),
    ]
