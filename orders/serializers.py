# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    district_name = serializers.CharField(source='district.name', read_only=True, default=None)

    def get_total_price(self, obj):
        return obj.get_total()

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'items', 'district_name', 'delivery_price', 'created_at']