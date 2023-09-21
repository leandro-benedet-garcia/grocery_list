from . import models, serializers

from rest_framework import viewsets


class ProductList(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.Product
