from django.db import models
from django.utils import timezone

class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    #filename = models.CharField(max_length=50, default="no_img.png")
    published = models.DateTimeField(default=timezone.now())
    bought = models.BooleanField(default=False)