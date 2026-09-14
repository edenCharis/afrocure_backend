# content/views.py
from rest_framework import generics, permissions
from .models import HomeContent, AboutContent
from .serializers import HomeContentSerializer, AboutContentSerializer


class HomeContentView(generics.RetrieveAPIView):
    serializer_class = HomeContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return HomeContent.load()


class AboutContentView(generics.RetrieveAPIView):
    serializer_class = AboutContentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return AboutContent.load()
