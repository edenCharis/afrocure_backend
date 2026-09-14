# backoffice/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AdminUserViewSet,
    AdminCategoryViewSet,
    AdminProductViewSet,
    AdminOrderViewSet,
    AdminOrderItemViewSet,
    AdminCartItemViewSet,
    AdminCountryViewSet,
    AdminCityViewSet,
    AdminDistrictViewSet,
    AdminHomeContentView,
    AdminAboutContentView,
    AdminProductsPageContentView,
    AdminLoginView,
    AdminLogoutView,
    AdminMeView,
)

router = DefaultRouter()
router.register(r'users', AdminUserViewSet, basename='admin-users')
router.register(r'categories', AdminCategoryViewSet, basename='admin-categories')
router.register(r'products', AdminProductViewSet, basename='admin-products')
router.register(r'orders', AdminOrderViewSet, basename='admin-orders')
router.register(r'order-items', AdminOrderItemViewSet, basename='admin-order-items')
router.register(r'cart-items', AdminCartItemViewSet, basename='admin-cart-items')
router.register(r'countries', AdminCountryViewSet, basename='admin-countries')
router.register(r'cities', AdminCityViewSet, basename='admin-cities')
router.register(r'districts', AdminDistrictViewSet, basename='admin-districts')

urlpatterns = [
    path('auth/login/', AdminLoginView.as_view(), name='admin-login'),
    path('auth/logout/', AdminLogoutView.as_view(), name='admin-logout'),
    path('auth/me/', AdminMeView.as_view(), name='admin-me'),
    path('home-content/', AdminHomeContentView.as_view(), name='admin-home-content'),
    path('about-content/', AdminAboutContentView.as_view(), name='admin-about-content'),
    path('products-page-content/', AdminProductsPageContentView.as_view(), name='admin-products-page-content'),
] + router.urls
