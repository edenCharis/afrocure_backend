# orders/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')
    
    def create(self, request):
        # Crée une commande depuis le panier actuel
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        
        if not cart_items.exists():
            return Response({'error': 'Panier vide'}, status=status.HTTP_400_BAD_REQUEST)
        
        total = sum(item.get_subtotal() for item in cart_items)
        order = Order.objects.create(user=request.user, total_price=total)
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.product.price
            )
        
        # Vider le panier après commande
        cart_items.delete()
        
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)