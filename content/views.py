# content/views.py
from rest_framework import generics, permissions
from .models import HomeContent
from .serializers import HomeContentSerializer


class HomeContentView(generics.RetrieveAPIView):
    serializer_class = HomeContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return HomeContent.load()
