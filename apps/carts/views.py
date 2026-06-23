from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.carts.models import Cart
from apps.carts.serializer import AddToCartSerializer, CartSerializer

from apps.carts.services import CartService


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        cart, _ = Cart.objects.get_or_create(
            user=request.user
        )

        serializer = CartSerializer(cart)

        return Response(serializer.data)


class CartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:
            cart = CartService.add_product(
                user=request.user,
                **serializer.validated_data,
            )
        except ValidationError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            CartSerializer(cart).data,
            status=status.HTTP_200_OK,
        )
