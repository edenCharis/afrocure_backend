# orders/notifications.py
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def send_whatsapp_notification(message: str):
    phone = getattr(settings, 'WHATSAPP_ADMIN_PHONE', None)
    api_key = getattr(settings, 'CALLMEBOT_API_KEY', None)

    if not phone or not api_key:
        logger.warning("WhatsApp notifications not configured (WHATSAPP_ADMIN_PHONE or CALLMEBOT_API_KEY missing).")
        return

    try:
        response = requests.get(
            "https://api.callmebot.com/whatsapp.php",
            params={"phone": phone, "text": message, "apikey": api_key},
            timeout=10,
        )
        if response.status_code != 200:
            logger.error(f"WhatsApp notification failed: {response.text}")
    except requests.RequestException as e:
        logger.error(f"WhatsApp notification error: {e}")


def notify_new_order(order):
    total = order.get_total()
    items_count = order.items.count()
    message = (
        f"🛍 Nouvelle commande #{order.id}\n"
        f"Client : {order.user.username}\n"
        f"Articles : {items_count}\n"
        f"Total : {total} XAF\n"
        f"Statut : {order.get_status_display()}"
    )
    send_whatsapp_notification(message)
