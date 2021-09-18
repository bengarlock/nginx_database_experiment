from rest_framework.serializers import ModelSerializer
from .models import Book, Guest, Slot, Restaurant, Table, Status, Floor


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
    class Meta:
        model = Table
        fields = '__all__'


class FloorSerializer(ModelSerializer):
    tables = TableSerializer(many=True, required=False)

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
