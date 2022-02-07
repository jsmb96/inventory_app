from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(default='Blank',max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(default='Blank',max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name