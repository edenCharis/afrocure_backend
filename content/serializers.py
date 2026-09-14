# content/serializers.py
from rest_framework import serializers
from .models import HomeContent, AboutContent, ProductsPageContent


class HomeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContent
        fields = '__all__'


class AboutContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutContent
        fields = '__all__'


class ProductsPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsPageContent
        fields = '__all__'
