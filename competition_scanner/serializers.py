from rest_framework import serializers
from .models import ResyRestaurant, ResyTotalCount, ResyGroup, YelpRestaurant, YelpTotals

class ResyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyRestaurant
        fields = '__all__'
        extra_kwargs = {"neighborhood": {"trim_whitespace": False}}


class ResyGroupSerializer(serializers.ModelSerializer):
    restaurants = ResyRestaurantSerializer(many=True, required=False)
    class Meta:
        model = ResyGroup
        fields = ["id", "name", "url", "restaurants", 'created_at', 'updated_at']


class ResyTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResyTotalCount
        fields = '__all__'


class YelpRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpRestaurant
        fields = '__all__'


class YelpTotalCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = YelpTotals
        fields = '__all__'
