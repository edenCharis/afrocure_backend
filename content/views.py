# content/views.py
from rest_framework import generics, permissions
from .models import HomeContent, AboutContent, ProductsPageContent
from .serializers import HomeContentSerializer, AboutContentSerializer, ProductsPageContentSerializer


class HomeContentView(generics.RetrieveAPIView):
    serializer_class = HomeContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return HomeContent.load()


class AboutContentView(generics.RetrieveAPIView):
    serializer_class = AboutContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return AboutContent.load()


class ProductsPageContentView(generics.RetrieveAPIView):
    serializer_class = ProductsPageContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return ProductsPageContent.load()
