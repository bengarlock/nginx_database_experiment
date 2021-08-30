from .models import ResyRestaurant, ResyTotalCount, YelpRestaurant, YelpTotals
from rest_framework import viewsets, permissions
from .serializers import ResyRestaurantSerializer, ResyTotalCountSerializer, \
    YelpRestaurantSerializer, YelpTotalCountSerializer
import django_filters.rest_framework


class ResyRestaurantViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    queryset = ResyRestaurant.objects.all()
    serializer_class = ResyRestaurantSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["resy_id", "created_at", "restaurant_name", "url"]

    #https://bengarlock.com/api/v1/resy/restaurants?resy_id=6822
    #https://bengarlock.com/api/v1/resy/restaurants/?created_at=2021-04-19T00:41:37.895084Z


class ResyTotalCountViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]
    queryset = ResyTotalCount.objects.all()
    serializer_class = ResyTotalCountSerializer

class YelpRestaurantViewSet(viewsets.ModelViewSet):
    queryset = YelpRestaurant.objects.all()
    serializer_class = YelpRestaurantSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["yelp_id", "created_at", "restaurant_name"]


class YelpTotalCountViewSet(viewsets.ModelViewSet):
    queryset = YelpTotals.objects.all()
    serializer_class = YelpTotalCountSerializer
