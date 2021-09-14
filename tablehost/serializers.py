from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table, Status, Floor


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class SlotSerializerWithGuest(serializers.ModelSerializer):
    guest = GuestSerializer(required=False)

    class Meta:
        model = Slot
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, required=False)

    class Meta:
        model = Floor
        fields = '__all__'
        fields = ['id', 'name', 'created_at', 'updated_at', 'tables']


class BookSerializer(serializers.ModelSerializer):
    slots = SlotSerializerWithGuest(many=True, required=False)
    floors = FloorSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'date', 'restaurant_id', 'created_at', 'updated_at', 'slots', 'floors']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
