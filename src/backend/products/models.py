from django.db import models

from djmoney.models.fields import MoneyField


CURRENCY_ARGS = {
    "max_digits": 19,
    "decimal_places": 4,
    "default_currency": "BRL",
}


class Grocery(models.Model):
    name = models.CharField()


class Brand(models.Model):
    name = models.CharField()


class Prices(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    grocery = models.ForeignKey(Grocery.__name__, models.CASCADE)

    bulk_amount = models.IntegerField()

    price = MoneyField(**CURRENCY_ARGS)
    bulk_cost = MoneyField(**CURRENCY_ARGS)


class Product(models.Model):
    name = models.CharField()
    brand = models.ForeignKey(Brand.__name__, models.CASCADE)
    prices = models.ForeignKey(Prices.__name__, models.CASCADE)
