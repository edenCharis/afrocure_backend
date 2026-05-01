# orders/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .notifications import notify_new_order


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        notify_new_order(instance)
