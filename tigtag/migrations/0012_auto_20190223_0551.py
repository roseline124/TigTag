# Generated by Django 2.1.7 on 2019-02-22 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tigtag', '0011_waitinglist_waiting_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitinglist',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to='tigtag.Customer'),
        ),
    ]
