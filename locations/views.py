# locations/views.py
from rest_framework import viewsets, permissions
from .models import Country, City, District
from .serializers import CountrySerializer, CitySerializer, DistrictSerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = City.objects.all().order_by('name')
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country_id=country)
        return queryset


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all().order_by('name')
    serializer_class = DistrictSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = District.objects.all().order_by('name')
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city_id=city)
        return queryset
