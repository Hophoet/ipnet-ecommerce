from django.db import models

#Item models
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/items', null=True, blank=True)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()