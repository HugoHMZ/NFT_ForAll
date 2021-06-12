from django.db import models
from django.utils import timezone

class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    published = models.DateTimeField(default=timezone.now())