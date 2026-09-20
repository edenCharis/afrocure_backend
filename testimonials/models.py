# testimonials/models.py
from django.db import models


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)  # 1-5
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author_name} ({self.rating}★)"
