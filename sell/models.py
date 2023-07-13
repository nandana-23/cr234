from django.db import models

# Create your models here.
class buy(models.Model):
    image=models.CharField(max_length=2000)
    name=models.CharField(max_length=200)
    price=models.FloatField()
    stock=models.IntegerField()
