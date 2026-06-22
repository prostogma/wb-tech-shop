from rest_framework import viewsets

from apps.products.models import Product
from apps.products.permissions import IsAdminOrReadOnly
from apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]