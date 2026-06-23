from rest_framework import serializers

from apps.carts.models import Cart, CartItem


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1)


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField(source="product.id", read_only=True)
    name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.DecimalField(
        source="product.price", read_only=True, max_digits=10, decimal_places=2
    )

    class Meta:
        model = CartItem
        fields = (
            "id",
            "product_id",
            "name",
            "price",
            "quantity",
        )


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "items",
            "created_at",
            "updated_at",
        )
