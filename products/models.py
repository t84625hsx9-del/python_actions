from django.db import models
class Product(models.Model):
    name=models.CharField("Name", max_length=255)
    price=models.DecimalField("Price", max_digits=5, decimal_places=2)

def __str__(self):
    return self.name