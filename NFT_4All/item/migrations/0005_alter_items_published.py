# Generated by Django 3.2.4 on 2021-06-13 16:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20210613_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 16, 34, 41, 950202, tzinfo=utc)),
        ),
    ]