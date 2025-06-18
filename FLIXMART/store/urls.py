from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, ReviewViewSet

from . import views



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('', include(router.urls)),
]