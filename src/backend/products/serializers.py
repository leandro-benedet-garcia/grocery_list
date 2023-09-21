from . import models
from rest_framework import serializers


class Grocery(serializers.ModelSerializer):
    class Meta:
        model = models.Grocery
        fields = "__all__"


class Brand(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class Prices(serializers.ModelSerializer):
    class Meta:
        model = models.Prices
        fields = "__all__"


class Product(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = "__all__"
        # exclude = ["prices", "brand"]
