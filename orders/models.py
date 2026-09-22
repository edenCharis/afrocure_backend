# orders/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]

    # Nullable: le panier ne requiert pas de connexion (commande "invité" envoyée ensuite via WhatsApp).
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    district = models.ForeignKey('locations.District', on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    phone = models.CharField(max_length=30, blank=True, default='')
    delivery_price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all()) + self.delivery_price

    def __str__(self):
        who = self.user.username if self.user else "Invité"
        return f"Commande #{self.id} - {who}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=0)  # XAF, no decimals

    def get_subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"