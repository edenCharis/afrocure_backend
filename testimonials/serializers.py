# testimonials/serializers.py
from rest_framework import serializers
from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    """Lecture publique : uniquement les avis approuvés (vue filtrée côté queryset)."""
    class Meta:
        model = Testimonial
        fields = ['id', 'author_name', 'rating', 'comment', 'created_at']


class TestimonialCreateSerializer(serializers.ModelSerializer):
    """Soumission publique : jamais approuvé automatiquement, en attente de modération."""
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Testimonial
        fields = ['author_name', 'rating', 'comment']

    def create(self, validated_data):
        validated_data['approved'] = False
        return super().create(validated_data)
