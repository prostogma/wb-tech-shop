from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = router.urls
