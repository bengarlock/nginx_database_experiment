from .models import ResyRestaurant, ResyTotalCount, YelpRestaurant, YelpTotals, ResyGroup
from rest_framework import viewsets, permissions
from .serializers import ResyRestaurantSerializer, ResyTotalCountSerializer, \
    YelpRestaurantSerializer, YelpTotalCountSerializer, ResyGroupSerializer
import django_filters.rest_framework


class ResyGroupViewSet(viewsets.ModelViewSet):
    queryset = ResyGroup.objects.all()
    serializer_class = ResyGroupSerializer


class ResyRestaurantViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     permissions.IsAuthenticated
    # ]

    queryset = ResyRestaurant.objects.all()
    serializer_class = ResyRestaurantSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["resy_id", "created_at", "restaurant_name", "url"]


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
