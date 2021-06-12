# Generated by Django 3.2.4 on 2021-06-12 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('published', models.DateTimeField(default=datetime.datetime(2021, 6, 12, 15, 2, 36, 531426))),
            ],
        ),
    ]
