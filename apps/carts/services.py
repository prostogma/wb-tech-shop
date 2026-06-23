from uuid import UUID

from django.db import transaction

from apps.products.models import Product

from apps.carts.models import Cart, CartItem


class CartService:
    @staticmethod
    @transaction.atomic
    def add_product(*, user, product_id: UUID, quantity: int):
        cart, _ = Cart.objects.get_or_create(user=user)

        product = Product.objects.get(id=product_id)

        item = CartItem.objects.filter(cart=cart, product=product).first()

        if item:
            new_quantity = item.quantity + quantity

            if new_quantity > product.stock:
                raise ValueError("Недостаточно товара на складе")

            item.quantity = new_quantity
            item.save(update_fields=["quantity"])

            return cart

        if quantity > product.stock:
            raise ValueError("Недостаточно товара на складе")

        CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        
        return cart
