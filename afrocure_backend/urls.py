# afrocure_backend/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products.views import ProductViewSet
from cart.views import CartViewSet
from orders.views import OrderViewSet
from locations.views import CountryViewSet, CityViewSet, DistrictViewSet
from content.views import HomeContentView, AboutContentView, ProductsPageContentView, FooterContentView
from testimonials.views import TestimonialListCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'districts', DistrictViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/home-content/', HomeContentView.as_view(), name='home-content'),
    path('api/about-content/', AboutContentView.as_view(), name='about-content'),
    path('api/products-page-content/', ProductsPageContentView.as_view(), name='products-page-content'),
    path('api/footer-content/', FooterContentView.as_view(), name='footer-content'),
    path('api/testimonials/', TestimonialListCreateView.as_view(), name='testimonials'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('accounts.urls')),
    path('api/backoffice/', include('backoffice.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)