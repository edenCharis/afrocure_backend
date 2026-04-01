# cart/serializers.py
from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.CharField(write_only=True)
    subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'subtotal']
    
    def get_subtotal(self, obj):
        return float(obj.get_subtotal())
    
    def create(self, validated_data):
        from products.models import Product
        product_id = validated_data.pop('product_id')
        product = Product.objects.get(id=product_id)
        user = self.context['request'].user
        
        cart_item, created = CartItem.objects.get_or_create(
            user=user, product=product,
            defaults={'quantity': validated_data.get('quantity', 1)}
        )
        if not created:
            cart_item.quantity += validated_data.get('quantity', 1)
            cart_item.save()
        return cart_item