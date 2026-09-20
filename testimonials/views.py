# testimonials/views.py
from rest_framework import generics, permissions
from .models import Testimonial
from .serializers import TestimonialSerializer, TestimonialCreateSerializer


class TestimonialListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Testimonial.objects.filter(approved=True)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TestimonialCreateSerializer
        return TestimonialSerializer
