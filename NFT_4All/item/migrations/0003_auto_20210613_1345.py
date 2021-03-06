# Generated by Django 3.2.4 on 2021-06-13 13:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('filename', models.CharField(default='no_img.png', max_length=50)),
                ('published', models.DateTimeField(default=datetime.datetime(2021, 6, 13, 13, 45, 33, 235456, tzinfo=utc))),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
