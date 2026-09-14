# content/serializers.py
from rest_framework import serializers
from .models import HomeContent, AboutContent, ProductsPageContent, FooterContent


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


class FooterContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterContent
        fields = '__all__'
