from rest_framework import serializers
from .models import Book, Guest, Slot, Restaurant, Table, Status, Floor


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-name']
        model = Status
        fields = '__all__'


class SlotSerializerWithGuest(serializers.ModelSerializer):
    guest = GuestSerializer(required=False)

    # status = StatusSerializer(required=False)

    class Meta:
        model = Slot
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class TableStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['width', 'height', 'background_color', 'border']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'class_name', 'name', 'status', 'style', 'floor', 'created_at', 'updated_at']
        expandable_fields = {
            'style': (TableStyleSerializer, {'many': True})
        }


class FloorSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, required=False)

    class Meta:
        model = Floor
        fields = ['id', 'name', 'book', 'tables', 'created_at', 'updated_at']


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
