# cart/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import CartItem
from .serializers import CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user).select_related('product')
    
    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        total = sum(item.get_subtotal() for item in items)
        return Response({'items': serializer.data, 'total': float(total)})
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)