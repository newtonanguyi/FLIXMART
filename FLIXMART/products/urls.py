from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, ProductViewSet, ProductImageViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = router.urls 