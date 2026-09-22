# orders/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer
from products.models import Product
from locations.models import District


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_permissions(self):
        # Le panier public ne requiert pas de connexion : la commande doit pouvoir
        # être enregistrée (statut "en attente") avant d'ouvrir WhatsApp.
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')

    def create(self, request):
        items = request.data.get('items') or []
        if not items:
            return Response({'error': 'Panier vide'}, status=status.HTTP_400_BAD_REQUEST)

        district = None
        district_id = request.data.get('district_id')
        if district_id:
            district = District.objects.filter(pk=district_id).first()

        user = request.user if request.user.is_authenticated else None

        order = Order.objects.create(
            user=user,
            district=district,
            delivery_price=district.delivery_price if district else 0,
        )

        for entry in items:
            product = Product.objects.filter(pk=entry.get('product_id')).first()
            if not product:
                continue
            try:
                quantity = max(1, int(entry.get('quantity', 1)))
            except (TypeError, ValueError):
                quantity = 1
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)

        if not order.items.exists():
            order.delete()
            return Response({'error': 'Produits invalides'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
