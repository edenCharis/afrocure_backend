# locations/models.py
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    dial_code = models.CharField(max_length=6, blank=True, default='')  # ex: "+242"

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # XAF

    def __str__(self):
        return self.name
