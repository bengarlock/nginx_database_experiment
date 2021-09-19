from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book, Guest, Slot, Restaurant, Table, Status, Floor
import json


# check out https://github.com/rsinger86/drf-flex-fields for nexsted updates

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class StatusSerializer(ModelSerializer):
    class Meta:
        ordering = ['-name']
        model = Status
        fields = '__all__'


class SlotSerializerWithGuest(ModelSerializer):
    guest = GuestSerializer(required=False)

    class Meta:
        model = Slot
        fields = '__all__'


class SlotSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'


class TableSerializer(ModelSerializer):
    style = serializers.SerializerMethodField('get_style')
    position = serializers.SerializerMethodField('get_position')
    floor = serializers.SerializerMethodField('get_floor')

    class Meta:
        model = Table
        fields = ('id', 'floor', 'class_name', 'name', 'style', 'position')

    def get_style(self, instance):
        style = {
            "width": instance.width,
            "height": instance.height,
            "background_color": instance.background_color,
            "border": instance.border,
        }
        return style

    def get_position(self, instance):
        position = {
            "left": instance.left,
            "top": instance.top
        }
        return position

    def get_floor(self, instance):
        floor = {
            "id": instance.floor.id,
            "name": instance.floor.name
        }
        return floor


class TableSerializerNoFloor(TableSerializer):
    class Meta:
        model = Table
        fields = ('id', 'class_name', 'name', 'style', 'position')


class FloorSerializer(ModelSerializer):
    tables = TableSerializerNoFloor(required=False, many=True)

    class Meta:
        model = Floor
        fields = ['id', 'name', 'book', 'tables', 'created_at', 'updated_at']


class BookSerializer(ModelSerializer):
    slots = SlotSerializerWithGuest(many=True, required=False)
    floors = FloorSerializer(many=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'date', 'restaurant_id', 'created_at', 'updated_at', 'slots', 'floors']


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']
