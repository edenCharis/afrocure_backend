# backoffice/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from products.models import Product, Category
from orders.models import Order, OrderItem
from cart.models import CartItem


class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login',
            'password',
        ]
        read_only_fields = ['date_joined', 'last_login']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JSONStringField(serializers.JSONField):
    """Accepts either a real JSON array or a JSON-encoded string (multipart/form-data)."""
    def to_internal_value(self, data):
        if isinstance(data, str):
            import json
            try:
                data = json.loads(data)
            except (ValueError, TypeError):
                self.fail('invalid')
        return super().to_internal_value(data)


class AdminProductSerializer(serializers.ModelSerializer):
    benefits = JSONStringField(default=list)
    usage = JSONStringField(default=list)
    ingredients = JSONStringField(default=list)

    class Meta:
        model = Product
        fields = '__all__'


class AdminOrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_name', 'quantity', 'price']


class AdminOrderSerializer(serializers.ModelSerializer):
    items = AdminOrderItemSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'username', 'email', 'status', 'total', 'items', 'created_at', 'updated_at']

    def get_total(self, obj):
        return float(obj.get_total())


class AdminCartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'username', 'product', 'product_name', 'quantity', 'subtotal', 'added_at']

    def get_subtotal(self, obj):
        return float(obj.get_subtotal())
